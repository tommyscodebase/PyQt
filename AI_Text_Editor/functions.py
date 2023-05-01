import openai
import env
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

openai.api_key = env.OPENAI_API_KEY


def new(ui):
    ui.textEdit.clear()
    ui.filename = None
    ui.statusbar.showMessage("A new file has bee created. make sure you save it")
    ui.setWindowTilte("Untitled -- Tommy's Docs")


def file_changed(filename, editor_text):
    with open(filename, 'r') as file:
        existing = file.read()
    return True if existing != editor_text else False


def send_to_openai(data):
    try:
        discussion = openai.Completion.create(
            prompt=data,
            engine="text-davinci-002",
            max_tokens=2040,
        )

        answer = discussion.choices[0].text
        return answer
    except Exception as e:
        print(f"Chatbot Error: {e}")


def about_app():
    msg = QMessageBox()
    msg.setWindowTitle("About Tommy's Docs")
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap('./resources/imgs/_app_icon.ico'),
        QtGui.QIcon.Normal, QtGui.QIcon.Off
    )
    msg.setWindowIcon(icon)
    msg.setText(
        "<p><b>Tommy's Docs</b> v1.0</p>"

        "This is an intelligent text editor built with Python.<br>"
        "<b>App Features</b>"
        "<ul>"
        "<li>Open, create and save new files.</li>"
        "<li>Export to PDF</li>"
        "<li>Print directly to a printer</li>"
        "<li>Save file before closing</li>"
        "<li>Text formatting.</li>"
        "<li>An interactive AI chat bot to assist you with your work</li>"
        "</ul>"
    )
    msg.exec_()


def about_me():
    msg = QMessageBox()
    msg.setWindowTitle("About Developer")
    icon = QtGui.QIcon()
    icon.addPixmap(
        QtGui.QPixmap('./resources/imgs/dev_info.png'),
        QtGui.QIcon.Normal, QtGui.QIcon.Off
    )
    msg.setWindowIcon(icon)
    msg.setText(
        "<p><b>Tommy's Docs</b> v1.0</p>"

        "<b>About the developer</b>"

        "<p>"
        "This app was made by Tommy"

        "Feel free to contact the developer for bug reports and feature suggestions.< br > "
        "<b>Developer Details</b><br>"
        "<b>Name:</b> Tommy<br>"
        "<b>Email:</b> tommy@mail.com"
        "You can visit his YouTube channel, <b>Tommy's Codebase</b><br><br>"

        "<b>Don't forget to subscribe and turn on notifications so that you don't miss any future tutorial</b>"

        "</p>"
    )
    msg.exec_()
