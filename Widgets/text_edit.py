import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTextEdit')

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        self.text = QTextEdit()
        self.btn = QPushButton('Print Text')

        layout.addWidget(self.text)
        layout.addWidget(self.btn)

        self.setCentralWidget(c_widget)

        # Connections
        self.btn.clicked.connect(self.function)

    def function(self):
        current_text = self.text.toPlainText()
        print(current_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
