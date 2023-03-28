from main import Editor
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = Editor()
sys.exit(app.exec())
