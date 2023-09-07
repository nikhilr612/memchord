import rtmidi
from threading import Thread
import time

class PlaybackThread(Thread):
	def __init__(self, settings):
		Thread.__init__(self, daemon=True);
		self.midi_program = settings['midi_prog'];
		self.settings = settings;
		self.messages = [];
		self.running = True;

	def queue_notes(self, notes, arpeggio=False):
		self.messages.insert(0, (notes, arpeggio));

	def run(self):
		midiout = rtmidi.RtMidiOut();
		midiout.openPort(0);
		midiout.sendMessage(rtmidi.MidiMessage.programChange(1, self.midi_program));
		while self.running:
			while len(self.messages):

				arpeggio_duration = self.settings['arpeggio_dur'];
				chord_duration = self.settings['chord_dur'];

				notes, is_arpeggio = self.messages.pop();
				for note in notes:
					midiout.sendMessage(rtmidi.MidiMessage.noteOn(1, note, 64));
					if is_arpeggio:
						time.sleep(arpeggio_duration);
				time.sleep(chord_duration)
				midiout.sendMessage(rtmidi.MidiMessage.allNotesOff(1));
		del midiout

	def close(self):
		self.running = False;

diatonic_scale_degree_idx_map = {
	1 : 0,
	2 : 2,
	3 : 4,
	4 : 5,
	5 : 7,
	6 : 9,
	7 : 11
}

chromatic_id_to_name_map = {
	0: 'C',
	1: 'C#/Db',
	2: 'D',
	3: 'D#/Eb',
	4: 'E/Fb',
	5: 'F/E#',
	6: 'F#/Gb',
	7: 'G',
	8: 'G#/Ab',
	9: 'A',
	10: 'A#/Bb',
	11: 'B/Cb'
}

def _scale_deg2pitch(tok):
	idx = int(tok);
	quot = idx >> 3;
	rem  = (idx & 7);
	rem = rem + 1 if quot > 0 else rem;
	return quot*12 + diatonic_scale_degree_idx_map[rem];

def pattern_to_notes(pat, base=0):
	notes = [];
	tokens = pat.strip().split(' ');
	for tok in tokens:
		if tok[-1] == '#':
			notes.append(base + _scale_deg2pitch(tok[:-1]) + 1);
		elif tok[-1] == 'b':
			notes.append(base + _scale_deg2pitch(tok[:-1]) - 1);
		else:
			notes.append(base + _scale_deg2pitch(tok));
	return notes;


def notes_to_names(notes):
	return [chromatic_id_to_name_map[note_id % 12] for note_id in notes];

if __name__ == "__main__":
	# Run tests
	assert pattern_to_notes("1 3 5") == [0, 4, 7];
	assert notes_to_names(pattern_to_notes("1 3 5")) == ['C', 'E/Fb', 'G'];
	assert pattern_to_notes("1 3b 5b 7b", 2) == [2, 5, 8, 12];
	assert notes_to_names(pattern_to_notes("1 3b 5", 9)) == ['A', 'C', 'E/Fb'];