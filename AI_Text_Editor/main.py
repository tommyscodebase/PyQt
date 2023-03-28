from PyQt5.QtWidgets import *
from editor import Ui_Editor


class Editor(QMainWindow, Ui_Editor):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        self.showMaximized()


