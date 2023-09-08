from cardview_window import Ui_MainWindow
from settings_dialog import Ui_Dialog
import sys, os, random
import json
from spsch import Scheduler
from PySide6 import QtWidgets
import playback

about_this = \
"""MemChord is a simple ear-training app that applies spaced repetition (SM-02) to present and (hopefully) \
aid the user in internalizing the sound associated with various chords and intervals.
"""

default_settings = {
	'arpeggio_dur': 0.1,
	'chord_dur'   : 2.0,
	'midi_prog'   : 0,
	'use_lilypond': False 
};

MIN_MIDI_NOTE = 43;
MAX_MIDI_NOTE = 81;

class SettingsDialog(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self, settings, parent=None):
		super().__init__();
		self.setupUi(self);
		self.settings = settings;
		self.arpegdurSpinBox.setValue(settings['arpeggio_dur']);
		self.arpegdurSpinBox.setSingleStep(0.05);
		self.chddurSpinBox.setSingleStep(0.05);
		self.chddurSpinBox.setValue(settings['chord_dur']);
		self.spinBox.setValue(settings['midi_prog']);
		self.applyButton.clicked.connect(self.apply_changes);
		self.restoreButton.clicked.connect(self.restore_settings);

	def apply_changes(self):
		self.settings['arpeggio_dur'] = self.arpegdurSpinBox.value();
		self.settings['chord_dur'] = self.chddurSpinBox.value();
		self.settings['midi_prog'] = self.spinBox.value();
		with open("./config.json", 'w') as f:
			json.dump(self.settings, f)

	def restore_settings(self):
		self.settings.update(default_settings);
		self.arpegdurSpinBox.setValue(settings['arpeggio_dur']);
		self.chddurSpinBox.setValue(settings['chord_dur']);
		self.spinBox.setValue(settings['midi_prog']);
		with open("./config.json", 'w') as f:
			json.dump(self.settings, f)

class App(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, playback_thread, settings):
		super().__init__()
		self.pbthread = playback_thread;
		self.settings = settings;
		self.setupUi(self);
		self.scheduler = None;
		self.currentCard = None;
		self.actionQuit.triggered.connect(self.quit_app);
		p = self.verticalWidget.sizePolicy();
		p.setRetainSizeWhenHidden(True);
		self.verticalWidget.setSizePolicy(p);
		self.verticalWidget.hide();
		self.revealBtn_5.clicked.connect(self.show_card_data);
		self.pushButton.clicked.connect(self.play_card);
		self.actionOpen_Deck.triggered.connect(self.open_deck);
		self.actionConfigure.triggered.connect(self.open_settings)
		self.actionAbout.triggered.connect(self.show_about_message);
		self.actionSchedule_Cards.triggered.connect(self.schedule_new_cards);

		self.useroption_0.clicked.connect(lambda: self.on_user_option(0));
		self.useroption_1.clicked.connect(lambda: self.on_user_option(1));
		self.useroption_2.clicked.connect(lambda: self.on_user_option(2));
		self.useroption_3.clicked.connect(lambda: self.on_user_option(3));
		self.useroption_4.clicked.connect(lambda: self.on_user_option(4));
		self.useroption_5.clicked.connect(lambda: self.on_user_option(5));

		self.deck_name_label.setText("No deck.");

	def on_user_option(self, q):
		assert self.scheduler is not None;
		assert self.currentCard is not None;
		card_id = self.currentCard[0];
		self.scheduler.record_response(card_id, q);

		self.verticalWidget.hide();
		self.useroption_0.setEnabled(False);
		self.useroption_1.setEnabled(False);
		self.useroption_2.setEnabled(False);
		self.useroption_3.setEnabled(False);
		self.useroption_4.setEnabled(False);
		self.useroption_5.setEnabled(False);
		self.revealBtn_5.setEnabled(True);

		self.try_poll_card();

	def show_about_message(self):
		msgBox = QtWidgets.QMessageBox();
		msgBox.setWindowTitle("About");
		if self.scheduler is None:
			msgBox.setText(about_this + "\nNo deck has been opened.");
		else:
			infotext = self.scheduler.deck.get('info', "The current deck has no description");
			msgBox.setText(about_this + "\n" + infotext)
		msgBox.exec();

	def play_card(self):
		if self.currentCard is None:
			return
		_, notes, is_arpeggio = self.currentCard;
		self.pbthread.queue_notes(notes, is_arpeggio);

	def open_settings(self):
		d = SettingsDialog(self.settings, self);
		d.exec();

	def quit_app(self):
		self.pbthread.close();
		if self.scheduler is not None:
			self.scheduler.save_progress();
		QtWidgets.QApplication.closeAllWindows();

	def show_card_data(self):
		if self.scheduler is None:
			return;
		if self.scheduler.num_scheduled() == 0:
			return;
		assert self.currentCard is not None;
		self.verticalWidget.show();
		self.useroption_0.setEnabled(True);
		self.useroption_1.setEnabled(True);
		self.useroption_2.setEnabled(True);
		self.useroption_3.setEnabled(True);
		self.useroption_4.setEnabled(True);
		self.useroption_5.setEnabled(True);
		self.revealBtn_5.setEnabled(False);

	def try_poll_card(self):
		if self.scheduler is None:
			return
		# Set label whenever card is polled.
		self.study_info_label_5.setText(self.scheduler.get_study_info());
		
		card = self.scheduler.poll_card();
		if card is not None:
			self.card_name_label_4.setText(card[1]['name']);
			self.cardinfo_text.setText(process_text_block(card[1]['notes']));
			pat = card[1]['pattern'];
			self.ppattern_label.setText("Pitch Pattern: " + pat);
			# #
			# TODO: Generate and set image by using lilypond.
			# #
			notes = playback.pattern_to_notes(pat, base=random.randint(MIN_MIDI_NOTE, MAX_MIDI_NOTE));
			self.cpitch_label.setText("Component pitches: " + ','.join(playback.notes_to_names(notes)));
			is_arpeggio = bool(random.getrandbits(1));
			if random.getrandbits(1) and is_arpeggio: # Randomly reverse note order 
				notes.reverse();
			self.currentCard = (card[0], notes, is_arpeggio);
		else:
			self.currentCard = None;


	def schedule_new_cards(self):
		if self.scheduler is None:
			msgBox = QtWidgets.QMessageBox(self);
			msgBox.setWindowTitle("Schedule New Cards");
			msgBox.setText("No deck selected. Please open a deck from [File->Open Deck] and then try again.");
			msgBox.exec();
		else:
			value, ok = QtWidgets.QInputDialog().getInt(self, "Schedule New Cards", "How many new cards to schedule?", value=1, minValue=0);
			if ok:
				self.scheduler.schedule_new_cards(value);
				if self.currentCard is None:
					self.try_poll_card();

	def open_deck(self):
		if self.scheduler is not None:
			self.scheduler.save_progress();

		dialog = QtWidgets.QFileDialog(self);
		dialog.setFileMode(QtWidgets.QFileDialog.AnyFile);
		dialog.setNameFilter("Decks (*.json *.txt)");
		if dialog.exec():
			deckpath = dialog.selectedFiles()[0];
			print("Selected file:", deckpath);
			self.scheduler = Scheduler(deckpath);
			self.deck_name_label.setText(self.scheduler.deck['name']);
			self.try_poll_card();


def process_text_block(text):
	lines = text.split('\n');
	if lines[0].strip() == '':
		lines = lines[1:]
	for i in range(len(lines[0])):
		if not lines[0][i].isspace():
			break;
	lines[0] = lines[0][i:]
	for j in range(1,len(lines)):
		lines[j] = lines[j][i:]
	ret = '\n'.join(lines);
	return ret

def show_ui(playback_thread, settings):
	qt_app = QtWidgets.QApplication(sys.argv);
	if os.path.exists("./style.qss"):
		with open("./style.qss") as f:
			qt_app.setStyleSheet(f.read())
	app = App(playback_thread, settings);
	app.show();
	qt_app.exec_();