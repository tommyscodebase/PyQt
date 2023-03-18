import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        self.setGeometry(500, 100, 500, 100)

        c_widget = QWidget()
        # Layouts
        layout_main = QHBoxLayout(c_widget)
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()

        layout_main.addLayout(layout_1)
        layout_main.addLayout(layout_2)

        self.btn_1 = QPushButton('Button1')
        layout_1.addWidget(self.btn_1)

        # LineEdits
        self.entry_1 = QLineEdit()
        layout_2.addWidget(self.entry_1)

        self.setCentralWidget(c_widget)

        # Connections
        self.entry_1.textChanged.connect(self.btn_1.setText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
