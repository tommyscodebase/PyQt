import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QToolBar, QAction, QTextEdit


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt Toolbar')
        self.setGeometry(500, 100, 500, 400)

        # Central Widget
        c_widget = QWidget()

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Toolbar Actions
        new_action = QAction(QIcon("icons/new.png"), "New", self)
        open_action = QAction(QIcon("icons/open.png"), "Open", self)
        save_action = QAction(QIcon("icons/save.png"), "Save", self)

        # Add action to toolbar
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Layouts
        main_layout = QVBoxLayout(c_widget)

        self.editor = QTextEdit()
        main_layout.addWidget(self.editor)

        # Set central widget
        self.setCentralWidget(c_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
