import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QT layouts')
        self.setGeometry(500, 100, 500, 100)

        c_widget = QWidget()
        # Layouts

        layout_main = QHBoxLayout(c_widget)
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()

        layout_main.addLayout(layout_1)
        layout_main.addLayout(layout_2)

        btn_1 = QPushButton('Button1')
        btn_2 = QPushButton('Button2')
        btn_3 = QPushButton('Button3')
        btn_4 = QPushButton('Button4')

        layout_1.addWidget(btn_1)
        layout_1.addWidget(btn_2)
        layout_1.addWidget(btn_3)
        layout_1.addWidget(btn_4)

        # LineEdits
        entry_1 = QLineEdit()
        entry_2 = QLineEdit()
        entry_3 = QLineEdit()
        entry_4= QLineEdit()

        layout_2.addWidget(entry_1)
        layout_2.addWidget(entry_2)
        layout_2.addWidget(entry_3)
        layout_2.addWidget(entry_4)

        self.setCentralWidget(c_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
