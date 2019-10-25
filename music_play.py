from PyQt5 import QtCore, QtGui, QtWidgets


class MusicPlay(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        pass
