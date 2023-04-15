def new(ui):
    ui.textEdit.clear()
    ui.filename = None
    ui.statusbar.showMessage("A new file has bee created. make sure you save it")
    ui.setWindowTilte("Untitled -- Tommy's Docs")


def file_changed(filename, editor_text):
    with open(filename, 'r') as file:
        existing = file.read()
    return True if existing != editor_text else False
