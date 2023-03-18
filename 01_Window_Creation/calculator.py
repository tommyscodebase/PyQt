import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Calculator')
        self.setGeometry(500, 100, 300, 100)
        # Central Widget
        c_widget = QWidget()

        # Layouts
        main_layout = QVBoxLayout(c_widget)
        top_layout = QVBoxLayout()
        bottom_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        # Widgets
        self.answer_box = QLineEdit()
        self.answer = QLabel('The answer is:')
        self.btn = QPushButton('Answer')

        top_layout.addWidget(self.answer_box)
        bottom_layout.addWidget(self.answer)
        bottom_layout.addWidget(self.btn)

        # Set central widget
        self.setCentralWidget(c_widget)

        # Connections
        self.btn.clicked.connect(self.set_answer)

    def set_answer(self):
        expression = self.answer_box.text()
        if len(expression) > 0:
            answer = eval(expression.strip())
            self.answer.setText(f'The answer is: {answer}')
        else:
            self.answer.setText(f'Enter an expression')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
