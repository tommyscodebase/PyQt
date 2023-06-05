from main_class import ImageConverter
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = ImageConverter()
sys.exit(app.exec())
