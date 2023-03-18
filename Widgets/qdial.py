import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDial


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDial')

        c_widget = QWidget()
        layout = QVBoxLayout(c_widget)

        self.dial = QDial()
        self.dial.setRange(0, 10)
        self.dial.setValue(4)
        self.dial.setNotchesVisible(True)

        layout.addWidget(self.dial)

        self.setCentralWidget(c_widget)

        # Connections
        self.dial.valueChanged.connect(self.function)

    def function(self, value):
        print(f'The value is: {value}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
