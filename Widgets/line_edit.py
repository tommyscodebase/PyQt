import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QHBoxLayout, QPushButton, QVBoxLayout


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('line edit')

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        self.entry = QLineEdit('Default text')
        # self.entry.setReadOnly(True)
        self.btn = QPushButton('Button')
        layout.addWidget(self.entry)
        layout.addWidget(self.btn)

        self.setCentralWidget(c_widget)

        # Connections
        self.btn.clicked.connect(self.function)

    def function(self):
        text = self.entry.text()
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
