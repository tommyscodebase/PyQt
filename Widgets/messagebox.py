import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QWidget, QVBoxLayout, QPushButton, QMessageBox


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMessageBox')

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        self.btn = QPushButton('Show Message')
        layout.addWidget(self.btn)

        self.setCentralWidget(c_widget)

        # Connections
        self.btn.clicked.connect(self.function)

    def function(self):
        msg = QMessageBox()
        msg.setWindowTitle('Info')
        msg.setText('This is a message box')
        msg.setDetailedText('This is a detailed text')
        msg.show()
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
