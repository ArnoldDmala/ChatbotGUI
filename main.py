from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
from backend import Chatbot
import sys
import threading

# iniitializing the window


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        # Dimensions in order - left, top, width, vertical
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        # Strip gets rid of any trailing spaces
        user_input = self.input_field.text().strip()

        # Puts the user input into the chat area
        self.chat_area.append(
            f"<p style = 'color: #333333'> Me: {user_input} </p>")

        self.input_field.clear()

        # threading to improve response times
        thread = threading.Thread(
            target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(
            f"<p style = 'color: #333333; background-color: #E9E9E9'> Bot: {response} </p>")


# instantiating Q Application
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
