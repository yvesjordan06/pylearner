# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\central_side.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CentralSide(object):
    def setupUi(self, CentralSide):
        CentralSide.setObjectName("CentralSide")
        CentralSide.resize(600, 544)
        self.verticalLayout = QtWidgets.QVBoxLayout(CentralSide)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.title_label = QtWidgets.QLabel(CentralSide)
        self.title_label.setStyleSheet("QLabel\n"
"{\n"
"     font-weight: bold;\n"
"     font-size: 18px;\n"
"}")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.video_player_frame = QtWidgets.QFrame(CentralSide)
        self.video_player_frame.setMinimumSize(QtCore.QSize(600, 248))
        self.video_player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_player_frame.setObjectName("video_player_frame")
        self.verticalLayout.addWidget(self.video_player_frame)
        self.frame_2 = QtWidgets.QFrame(CentralSide)
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"      background-color: #28d;\\n\n"
" }")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backward_button = QtWidgets.QPushButton(self.frame_2)
        self.backward_button.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"}")
        self.backward_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/md-skip-backward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backward_button.setIcon(icon)
        self.backward_button.setObjectName("backward_button")
        self.horizontalLayout_2.addWidget(self.backward_button)
        self.play_button = QtWidgets.QPushButton(self.frame_2)
        self.play_button.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"}")
        self.play_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/svg/icons8-play-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_2.addWidget(self.play_button)
        self.forward_buttton = QtWidgets.QPushButton(self.frame_2)
        self.forward_buttton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: transparent;\n"
"}")
        self.forward_buttton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/svg/md-skip-forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward_buttton.setIcon(icon2)
        self.forward_buttton.setObjectName("forward_buttton")
        self.horizontalLayout_2.addWidget(self.forward_buttton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_2)
        self.scrollArea = QtWidgets.QScrollArea(CentralSide)
        self.scrollArea.setStyleSheet("QScrollArea\n"
"{\n"
"    border: none;\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 583, 310))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comment_title_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.comment_title_label.setStyleSheet("QLabel\n"
"{\n"
"  font-weight: bold;\n"
"}")
        self.comment_title_label.setObjectName("comment_title_label")
        self.verticalLayout_2.addWidget(self.comment_title_label)
        self.comment_content_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.comment_content_label.setObjectName("comment_content_label")
        self.verticalLayout_2.addWidget(self.comment_content_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(CentralSide)
        QtCore.QMetaObject.connectSlotsByName(CentralSide)

    def retranslateUi(self, CentralSide):
        _translate = QtCore.QCoreApplication.translate
        CentralSide.setWindowTitle(_translate("CentralSide", "Form"))
        self.title_label.setText(_translate("CentralSide", "Title"))
        self.comment_title_label.setText(_translate("CentralSide", "Commentaires:"))
        self.comment_content_label.setText(_translate("CentralSide", "If that address is correct, here are three other things you can try:\n"
"\n"
"    Try again later.\n"
"\n"
"    Check your network connection.\n"
"    \n"
"    If you are connected but behind a firewall, check that Firefox has permission to access the Web.\n"
"    But you should know that i don\'t give a fuck about what they think about me\n"
"    I am a though nigga and I can shit everybody for your love\n"
"    Je ne sais meme plus quoi ecrire mais je veux juste remplir les lignes\n"
"    Ce motherfucker texte me fiche deje les jetons. J\'en ai marre\n"
"    Aparement je dois continuer d\'ecrire je ne sais quoi\n"
"    Mais il faut quand meme que je continue\n"
"    Je ne sais pas si tout va bien mais ca ira sans aucun doute\n"
"    Je suis sure que tout ira bien\n"
"    Je ne sais pas qui est Malcomn X\n"
"    Davido est un chanteur Africain et Chris Brown un Americain\n"
"\n"
"    Drake est mon meilleur rappeur US. J\'aime pratiquement tous ces sons\n"
"    Je ne suis pas un musicien de quel que sorte que ce soit car je sne suis pas talentueux\n"
"    Je pourrai bien entrainer mes enfants plus tard a jouer des instruments car c\'est bien pour ameliorer leur QI"))

from . import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CentralSide = QtWidgets.QWidget()
    ui = Ui_CentralSide()
    ui.setupUi(CentralSide)
    CentralSide.show()
    sys.exit(app.exec_())
