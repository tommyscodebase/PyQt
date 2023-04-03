import os.path

from PyQt5.QtWidgets import *
from editor import Ui_Editor
from functions import *


class Editor(QMainWindow, Ui_Editor):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        self.showMaximized()

        # Globals
        self.filename = None
        self.path = ''

        # Inits
        self.update_title()
        self.chatbot_frame.hide()

        # Connections
        self.actionOpen_Assistant.triggered.connect(self.open_chatbot)
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)

    # Functions
    # Set window title
    def update_title(self):
        if self.filename:
            self.setWindowTitle(f"{self.filename} -- Tommy's Docs")
        else:
            self.setWindowTitle("Untitled -- Tommy's Docs")

    # Show and hide chatbot
    def open_chatbot(self):
        try:
            if self.chatbot_frame.isVisible():
                self.chatbot_frame.hide()
            else:
                self.chatbot_frame.show()
        except Exception as e:
            print(f"Open chatbot error: {e}")

    # New file
    def new_file(self):
        try:
            if len(self.textEdit.toPlainText().strip()) != 0:
                prompt = QMessageBox.question(self, 'New File Dialog',
                                              "This will clear current content. Continue?",
                                              QMessageBox.Yes | QMessageBox.No
                                              )
                if prompt == QMessageBox.Yes:
                    new(self)
            else:
                new(self)
        except Exception as e:
            print(f"New file creation error: {e}")

    # Open File
    def open_file(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, 'Open a File', ':\\')

            if path:
                self.path = path
                with open(path, 'r') as file:
                    content = file.read()
                    self.textEdit.setText(content)
                    self.filename = os.path.basename(self.path)
                    self.update_title()

        except Exception as e:
            print(f"File opening error: {e}")
