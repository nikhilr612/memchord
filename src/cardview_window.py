# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardviewxkqmCB.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 601)
        MainWindow.setMinimumSize(QSize(0, 40))
        self.actionOpen_Deck = QAction(MainWindow)
        self.actionOpen_Deck.setObjectName(u"actionOpen_Deck")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionConfigure = QAction(MainWindow)
        self.actionConfigure.setObjectName(u"actionConfigure")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSchedule_Cards = QAction(MainWindow)
        self.actionSchedule_Cards.setObjectName(u"actionSchedule_Cards")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonsFrame = QFrame(self.centralwidget)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setMinimumSize(QSize(220, 0))
        self.verticalLayout_7 = QVBoxLayout(self.buttonsFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.deck_name_label = QLabel(self.buttonsFrame)
        self.deck_name_label.setObjectName(u"deck_name_label")
        self.deck_name_label.setMinimumSize(QSize(0, 40))
        self.deck_name_label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(15)
        self.deck_name_label.setFont(font)

        self.verticalLayout_7.addWidget(self.deck_name_label)

        self.study_info_label_5 = QLabel(self.buttonsFrame)
        self.study_info_label_5.setObjectName(u"study_info_label_5")
        self.study_info_label_5.setMinimumSize(QSize(0, 70))
        self.study_info_label_5.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.study_info_label_5.setFont(font1)

        self.verticalLayout_7.addWidget(self.study_info_label_5)

        self.useroption_0 = QPushButton(self.buttonsFrame)
        self.useroption_0.setObjectName(u"useroption_0")
        self.useroption_0.setEnabled(False)
        self.useroption_0.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_0)

        self.useroption_1 = QPushButton(self.buttonsFrame)
        self.useroption_1.setObjectName(u"useroption_1")
        self.useroption_1.setEnabled(False)
        self.useroption_1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_1)

        self.useroption_2 = QPushButton(self.buttonsFrame)
        self.useroption_2.setObjectName(u"useroption_2")
        self.useroption_2.setEnabled(False)
        self.useroption_2.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_2)

        self.useroption_3 = QPushButton(self.buttonsFrame)
        self.useroption_3.setObjectName(u"useroption_3")
        self.useroption_3.setEnabled(False)
        self.useroption_3.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_3)

        self.useroption_4 = QPushButton(self.buttonsFrame)
        self.useroption_4.setObjectName(u"useroption_4")
        self.useroption_4.setEnabled(False)
        self.useroption_4.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_4)

        self.useroption_5 = QPushButton(self.buttonsFrame)
        self.useroption_5.setObjectName(u"useroption_5")
        self.useroption_5.setEnabled(False)
        self.useroption_5.setMinimumSize(QSize(0, 40))

        self.verticalLayout_7.addWidget(self.useroption_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.pushButton = QPushButton(self.buttonsFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout_7.addWidget(self.pushButton)

        self.revealBtn_5 = QPushButton(self.buttonsFrame)
        self.revealBtn_5.setObjectName(u"revealBtn_5")
        self.revealBtn_5.setMinimumSize(QSize(0, 60))

        self.verticalLayout_7.addWidget(self.revealBtn_5)


        self.horizontalLayout.addWidget(self.buttonsFrame)

        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.card_name_label_4 = QLabel(self.verticalWidget)
        self.card_name_label_4.setObjectName(u"card_name_label_4")
        self.card_name_label_4.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(20)
        self.card_name_label_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.card_name_label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.chord_image = QLabel(self.verticalWidget)
        self.chord_image.setObjectName(u"chord_image")
        self.chord_image.setMinimumSize(QSize(0, 200))

        self.verticalLayout_8.addWidget(self.chord_image)

        self.cpitch_label = QLabel(self.verticalWidget)
        self.cpitch_label.setObjectName(u"cpitch_label")

        self.verticalLayout_8.addWidget(self.cpitch_label)

        self.ppattern_label = QLabel(self.verticalWidget)
        self.ppattern_label.setObjectName(u"ppattern_label")

        self.verticalLayout_8.addWidget(self.ppattern_label)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_5)

        self.cardinfo_text = QTextBrowser(self.verticalWidget)
        self.cardinfo_text.setObjectName(u"cardinfo_text")
        self.cardinfo_text.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.cardinfo_text.setFont(font3)

        self.verticalLayout_8.addWidget(self.cardinfo_text)


        self.horizontalLayout.addWidget(self.verticalWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 884, 22))
        self.menuOpen = QMenu(self.menubar)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOpen.addAction(self.actionOpen_Deck)
        self.menuOpen.addAction(self.actionQuit)
        self.menuOptions.addAction(self.actionSchedule_Cards)
        self.menuOptions.addAction(self.actionConfigure)
        self.menuOptions.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MemChord", None))
        self.actionOpen_Deck.setText(QCoreApplication.translate("MainWindow", u"Open Deck", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_Deck.setToolTip(QCoreApplication.translate("MainWindow", u"Open a deck to review", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen_Deck.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Save progress and Exit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionConfigure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
#if QT_CONFIG(shortcut)
        self.actionConfigure.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSchedule_Cards.setText(QCoreApplication.translate("MainWindow", u"Schedule New", None))
#if QT_CONFIG(shortcut)
        self.actionSchedule_Cards.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.deck_name_label.setText(QCoreApplication.translate("MainWindow", u"Deck Name", None))
        self.study_info_label_5.setText(QCoreApplication.translate("MainWindow", u"Study Info", None))
#if QT_CONFIG(tooltip)
        self.useroption_0.setToolTip(QCoreApplication.translate("MainWindow", u"Total blackout, no idea", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_0.setText(QCoreApplication.translate("MainWindow", u"Sounds New", None))
#if QT_CONFIG(tooltip)
        self.useroption_1.setToolTip(QCoreApplication.translate("MainWindow", u"Incorrect answer, but the correct answer feels familiar", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_1.setText(QCoreApplication.translate("MainWindow", u"Makes sense", None))
#if QT_CONFIG(tooltip)
        self.useroption_2.setToolTip(QCoreApplication.translate("MainWindow", u"Incorrect response, correct answer was wrongfully dismissed", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_2.setText(QCoreApplication.translate("MainWindow", u"Almost had it", None))
#if QT_CONFIG(tooltip)
        self.useroption_3.setToolTip(QCoreApplication.translate("MainWindow", u"Correct response, but required significant efforts", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_3.setText(QCoreApplication.translate("MainWindow", u"Almost missed it", None))
#if QT_CONFIG(tooltip)
        self.useroption_4.setToolTip(QCoreApplication.translate("MainWindow", u"Correct response, but after some hesitation", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_4.setText(QCoreApplication.translate("MainWindow", u"I got it, I think", None))
#if QT_CONFIG(tooltip)
        self.useroption_5.setToolTip(QCoreApplication.translate("MainWindow", u"Perfect response", None))
#endif // QT_CONFIG(tooltip)
        self.useroption_5.setText(QCoreApplication.translate("MainWindow", u"I got it", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Play Audio", None))
#if QT_CONFIG(tooltip)
        self.revealBtn_5.setToolTip(QCoreApplication.translate("MainWindow", u"Reveal the card", None))
#endif // QT_CONFIG(tooltip)
        self.revealBtn_5.setText(QCoreApplication.translate("MainWindow", u"Reveal", None))
#if QT_CONFIG(tooltip)
        self.card_name_label_4.setToolTip(QCoreApplication.translate("MainWindow", u"The name of the card", None))
#endif // QT_CONFIG(tooltip)
        self.card_name_label_4.setText(QCoreApplication.translate("MainWindow", u"Card Name", None))
#if QT_CONFIG(tooltip)
        self.chord_image.setToolTip(QCoreApplication.translate("MainWindow", u"Image related to the card", None))
#endif // QT_CONFIG(tooltip)
        self.chord_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.cpitch_label.setText(QCoreApplication.translate("MainWindow", u"Component Pitches:", None))
        self.ppattern_label.setText(QCoreApplication.translate("MainWindow", u"Pitch Pattern:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
#if QT_CONFIG(tooltip)
        self.cardinfo_text.setToolTip(QCoreApplication.translate("MainWindow", u"Notes pertaining to the card", None))
#endif // QT_CONFIG(tooltip)
        self.cardinfo_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Card Info</span></p></body></html>", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

