import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
