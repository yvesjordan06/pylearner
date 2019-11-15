from PyQt5 import QtWidgets, QtCore
from left_side import LeftSide
from central_side import CentralSide
from right_side import RightSide
from assets.ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(400, 300)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.layout = QtWidgets.QHBoxLayout(self.ui.main_page)
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.left_side = LeftSide()
        self.splitter.addWidget(self.left_side)
        self.central_side = CentralSide()
        self.splitter.addWidget(self.central_side)
        self.right_side = RightSide()
        self.splitter.addWidget(self.right_side)
        self.layout.addWidget(self.splitter)
        
        
        
if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
