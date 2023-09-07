# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialogzwzSbO.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 210)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.arpegdurSpinBox = QDoubleSpinBox(Dialog)
        self.arpegdurSpinBox.setObjectName(u"arpegdurSpinBox")

        self.horizontalLayout.addWidget(self.arpegdurSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.chddurSpinBox = QDoubleSpinBox(Dialog)
        self.chddurSpinBox.setObjectName(u"chddurSpinBox")

        self.horizontalLayout_2.addWidget(self.chddurSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setMaximumSize(QSize(80, 60))

        self.horizontalLayout_3.addWidget(self.applyButton)

        self.restoreButton = QPushButton(Dialog)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setMaximumSize(QSize(120, 60))

        self.horizontalLayout_3.addWidget(self.restoreButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Playback Settings:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Dialog", u"The time in seconds between succesive notes of an arpeggio", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Arpeggiation Duration:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Dialog", u"The total duration of a chord in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Chord Duration:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"MIDI Program:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Other:", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Dialog", u"If set, lilypond will be used to generate notation for chords", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Use lilypond", None))
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.restoreButton.setText(QCoreApplication.translate("Dialog", u"Restore Defaults", None))
    # retranslateUi

