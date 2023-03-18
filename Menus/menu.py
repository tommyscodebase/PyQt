import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QToolBar, QAction, QTextEdit


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt Menubar')
        self.setGeometry(500, 100, 500, 400)

        # Central Widget
        c_widget = QWidget()

        # Menubar
        menubar = self.menuBar()

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Toolbar Actions
        new_action = QAction(QIcon("icons/new.png"), "New", self)
        new_action.setShortcut('Ctrl+N')
        open_action = QAction(QIcon("icons/open.png"), "Open", self)
        open_action.setShortcut("Ctrl+O")
        save_action = QAction(QIcon("icons/save.png"), "Save", self)
        save_action.setShortcut("Ctrl+S")
        quit_action = QAction("Quit", self)
        quit_action.setShortcut("Ctrl+Q")

        copy_action = QAction(QIcon("icons/copy.png"), "Copy", self)
        copy_action.setShortcut('Ctrl+C')
        cut_action = QAction(QIcon("icons/cut.png"), "Cut", self)
        cut_action.setShortcut("Ctrl+X")
        paste_action = QAction(QIcon("icons/paste.png"), "Paste", self)
        paste_action.setShortcut("Ctrl+V")

        # Add action to toolbar
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Create menu items
        file_menu = menubar.addMenu('File')

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)

        # Edit menu
        edit_menu = menubar.addMenu('Edit')

        edit_menu.addAction(copy_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(paste_action)

        # Layouts
        main_layout = QVBoxLayout(c_widget)

        self.editor = QTextEdit()
        main_layout.addWidget(self.editor)

        # Set central widget
        self.setCentralWidget(c_widget)

        # Connections
        quit_action.triggered.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
