import os.path

from PyQt5.QtWidgets import *
from main import Ui_ImaCon


class ImageConverter(QMainWindow, Ui_ImaCon):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        self.images = []

        # Connections
        self.actionAdd_Images.triggered.connect(self.add_images)
        self.actionRemove_Selected.triggered.connect(self.remove_selected)
        self.actionRemove_All.triggered.connect(self.remove_all)

    # Add Images
    def add_images(self):
        try:
            files, _ = QFileDialog.getOpenFileNames(self, "Add Images", ":\\")

            if files:
                for image in files:
                    self.images.append(image)
                    self.listWidget.addItem(os.path.basename(image))
        except Exception as e:
            print(f"File opening error: {e}")

    # Remove Selected Image
    def remove_selected(self):
        try:
            if len(self.images) != 0:
                index = self.listWidget.currentRow()
                self.listWidget.takeItem(index)
                self.images.pop(index)
        except Exception as e:
            print(f"Removing Image Error: {e}")

    # Remove All Images
    def remove_all(self):
        try:
            if len(self.images) != 0:
                question = QMessageBox.question(
                    self, "Delete Confirmation",
                    "This will delete all images.\nContinue?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )

                if question == QMessageBox.Yes:
                    self.listWidget.clear()
                    self.images.clear()
        except Exception as e:
            print(f"Removing Images Error: {e}")
