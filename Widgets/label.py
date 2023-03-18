import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel: Display an Image')

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        label = QLabel()
        pixmap = QPixmap('cube.jpg').scaled(300, 200)
        label.setPixmap(pixmap)

        layout.addWidget(label)

        self.setCentralWidget(c_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
