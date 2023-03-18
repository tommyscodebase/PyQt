import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        c_widget = QWidget()
        layout = QHBoxLayout(c_widget)

        self.btn = QPushButton('My Button')
        layout.addWidget(self.btn)

        self.setCentralWidget(c_widget)

        # Connections
        self.btn.clicked.connect(self.function)

    def function(self):
        print('Button is clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
