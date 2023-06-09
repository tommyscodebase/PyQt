import os.path
import subprocess

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from main import Ui_ImaCon
from PIL import Image


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
        self.listWidget.itemClicked.connect(
            lambda: self.create_thumbnail(self.images[self.listWidget.currentRow()])
        )
        self.convert_btn.clicked.connect(self.convert_images)

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

    # Image Thumbnail
    def create_thumbnail(self, image):
        try:
            self.thumbnail_label.setPixmap(QtGui.QPixmap(image))
            self.image_details()
        except Exception as e:
            print(f"Creating thumbnail error: {e}")

    # Image Details
    def image_details(self):
        try:
            index = self.listWidget.currentRow()
            image = self.images[index]

            file_size = os.path.getsize(image)

            # Convert file size to KB or MB
            if file_size < 1024:
                size = f"{round(file_size, 2)} bytes"
            elif file_size < 1024 * 1024:
                size = f"{round(file_size / 1024, 2)} KB"
            else:
                size = f"{round(file_size / (1024 * 1024), 2)} MB"

            # Image dimensions
            img = Image.open(image)
            x, y = img.size
            self.img_details_textEdit.clear()
            self.img_details_textEdit.insertPlainText(
                f"Name: {os.path.basename(image)}\n"
                f"Location: {os.path.dirname(image)}\n"
                f"Size: {size}\n"
                f"Width: {x} pixels\n"
                f"Height: {y} pixels".strip()

            )
        except Exception as e:
            print(f"Image details error: {e}")

    def convert_images(self):
        # Check if images are loaded
        if len(self.images) == 0:
            QMessageBox.warning(
                self, "Conversion Error",
                "No images have been loaded. Load images before converting"
            )
            return
        # Check if a valid extension is selected
        if self.comboBox.currentText() == "":
            QMessageBox.warning(
                self, "Output Extension Error",
                "Select a valid a extension to continue"
            )
            return

        try:
            extension = f".{self.comboBox.currentText()}"
            path = QFileDialog.getExistingDirectory(self, "Select where to save files")

            if path:
                for image in self.images:
                    img = Image.open(image)
                    output_img = os.path.join(
                        path,
                        f"{os.path.basename(image).split('.')[0]}{extension}"
                    )
                    img.save(output_img)

                question = QMessageBox.question(
                    self, "Successful Conversion",
                    "Image(s) have been converted successfully.\n"
                    "Do you want to open the output folder?",
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No
                )
                if question == QMessageBox.Yes:
                    path_ = os.path.relpath(path)
                    subprocess.Popen(f"explorer {path_}")
        except Exception as e:
            print(f"Image Conversion Error: {e}")
