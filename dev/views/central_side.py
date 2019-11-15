from PyQt5 import QtWidgets, QtMultimedia, QtMultimediaWidgets, QtCore

from assets.central_side_ui import Ui_CentralSide



class CentralSide(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(CentralSide, self).__init__(parent)
        self.ui = Ui_CentralSide()
        self.ui.setupUi(self)
        
        self.media_player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        
        self.media_player.setVideoOutput(self.video_widget)
        
        self.frame_layout = QtWidgets.QVBoxLayout(self.ui.video_player_frame)
        
        self.frame_layout.addWidget(self.video_widget)
        
        self.media_player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("video.mp4")))
        
        
        
        
        
if __name__=='__main__':
    
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    ui = CentralSide()
    ui.show()
    sys.exit(app.exec_())