from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys

# iniitializing the window


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        # Dimensions in order - left, top, width, vertical
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.show()


class Chatbot:
    pass


# instantiating Q Application
app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())