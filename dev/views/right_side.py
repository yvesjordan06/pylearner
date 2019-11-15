from PyQt5 import QtWidgets, QtCore, QtGui
from assets.ui_right_side import Ui_RightSide
from assets import icons_rc


class RightSide(QtWidgets.QWidget):
    code_clicked = QtCore.pyqtSignal()
    question_clicked = QtCore.pyqtSignal()
    python_clicked = QtCore.pyqtSignal()
    github_clicked = QtCore.pyqtSignal()
    telegram_clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(RightSide, self).__init__(parent)
        self.ui = Ui_RightSide()
        self.ui.setupUi(self)
        self.ui.code_frame.clicked.connect(self.essai)

    def essai(self):
        print("Je suis le resultat du test")





if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rs = RightSide()
    rs.show()
    sys.exit(app.exec_())