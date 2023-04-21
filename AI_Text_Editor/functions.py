import openai
import env

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
