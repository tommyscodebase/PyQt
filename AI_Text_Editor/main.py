import os.path

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QFileInfo, QTime, QDate
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
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
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_file_as)
        self.actionBold.triggered.connect(self.bold)
        self.actionItalics.triggered.connect(self.italics)
        self.actionUnderline.triggered.connect(self.underline)
        self.actionAlign_Left.triggered.connect(self.align_left)
        self.actionAlign_Center.triggered.connect(self.align_center)
        self.actionAlign_Right.triggered.connect(self.align_right)
        self.actionAlign_Justify.triggered.connect(self.align_justify)
        self.fontcombo.activated.connect(self.font_family)
        self.font_size.valueChanged.connect(self.set_font_size)
        self.actionFont_Options.triggered.connect(self.font_options)
        self.actionChange_Font_Color.triggered.connect(self.text_color)
        self.actionChange_Background_Color.triggered.connect(self.bg_color)
        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.print_preview)
        self.actionExport_to_PDF.triggered.connect(self.export_to_pdf)
        self.actionInsert_Time.triggered.connect(self.insert_time)
        self.actionInsert_Date.triggered.connect(self.insert_date)

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

    # Save file
    def save_file(self):
        try:
            if self.path == '':  # If no file is opened, the call save as function
                self.save_file_as()

            content = self.textEdit.toPlainText().strip()

            with open(self.path, 'w') as file:
                file.write(content)
                self.statusbar.showMessage(f'{self.filename} has been saved successfully')
                self.update_title()
        except Exception as e:
            print(f'Error Saving file: {e}')

    # Save As
    def save_file_as(self):
        try:
            path, _ = QFileDialog.getSaveFileName(self, 'Save File As', ':\\',
                                                  "Text Files (*.txt);; All Files (*.*)"
                                                  )
            if path:
                content = self.textEdit.toPlainText().strip()
                self.path = path
                self.filename = os.path.basename(self.path)
                with open(self.path, 'w') as file:
                    file.write(content)
                    self.statusbar.showMessage(f'{self.filename} has been saved successfully')
                    self.update_title()
        except Exception as e:
            print(f'Error Saving file as: {e}')

    # Bold
    def bold(self):
        if self.textEdit.fontWeight() == QFont.Bold:
            self.textEdit.setFontWeight(QFont.Normal)
        else:
            self.textEdit.setFontWeight(QFont.Bold)

    # Italics
    def italics(self):
        if self.textEdit.fontItalic() == QFont.StyleItalic:
            self.textEdit.setFontItalic(False)
        else:
            self.textEdit.setFontItalic(True)

    # Underline
    def underline(self):
        state = self.textEdit.fontUnderline()
        self.textEdit.setFontUnderline(not state)

    # Left Align
    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    # Center Align
    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    # Right Align
    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    # Align Justify
    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    # Change text color
    def text_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    # Change background color
    def bg_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextBackgroundColor(color)

    # Change font family
    def font_family(self):
        font = self.fontcombo.currentText()
        self.textEdit.setCurrentFont(QFont(font))

    # Change font size
    def set_font_size(self):
        size = self.font_size.value()
        self.textEdit.setFontPointSize(size)

    # Font Options
    def font_options(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    # Print File
    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        prompt = QPrintDialog(printer, self)

        if prompt.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def preview(self, printer):
        self.textEdit.print_(printer)

    # Print Preview
    def print_preview(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintPreviewDialog(printer, self)
        dialog.paintRequested.connect(self.preview)
        dialog.exec_()

    # Export to PDF
    def export_to_pdf(self):
        file, _ = QFileDialog.getSaveFileName(self, "Export to PDF", ':\\',
                                              'PDF Files (*.pdf);; All Files (*.*)'
                                              )
        if file:
            if QFileInfo(file).suffix() == "":
                file += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file)
            self.textEdit.document().print_(printer)

    # Insert Current Time
    def insert_time(self):
        time = QTime.currentTime()
        self.textEdit.insertPlainText(time.toString(Qt.DefaultLocaleLongDate))

    # Insert Current Date
    def insert_date(self):
        date = QDate.currentDate()
        self.textEdit.insertPlainText(date.toString(Qt.DefaultLocaleLongDate))
