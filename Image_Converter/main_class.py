from PyQt5.QtWidgets import *
from main import Ui_ImaCon


class ImageConverter (QMainWindow, Ui_ImaCon):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()
