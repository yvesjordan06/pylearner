from PyQt5 import QtWidgets, QtCore
from assets.ui_main_window import Ui_MainWindow
from central_side import CentralSide
from left_side import LeftSide
from right_side import RightSide


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 300)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menubar.hide()
        self.layout = QtWidgets.QHBoxLayout(self.ui.main_page)
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.left_side = LeftSide()
        self.splitter.addWidget(self.left_side)
        self.central_side = CentralSide()
        self.splitter.addWidget(self.central_side)
        self.right_side = RightSide()
        self.splitter.addWidget(self.right_side)
        self.layout.addWidget(self.splitter)
        self.ui.pushButton.clicked.connect(self.connexion)
        self.ui.actionOuvrir.triggered.connect(self.open_file)

    def connexion(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.menubar.show()

    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Movie",
                                                            QtCore.QDir.homePath() + "/Videos",
                                                            "Media (*.webm *.mp4 *.ts *.avi *.mpeg *.mpg *.mkv *.VOB "
                                                            "*.m4v *.3gp *.mp3 *.m4a *.wav *.ogg *.flac *.m3u *.m3u8)")

        if fileName:
            self.central_side.open_file(fileName)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
