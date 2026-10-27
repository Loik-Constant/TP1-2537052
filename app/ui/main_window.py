import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QLabel, QWidget, QListWidget, \
    QListWidgetItem, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QTimer

from app.core.PasswordGenerator import PasswordGenerator


class MainWindow(QMainWindow):
    """
    Fenêtre principale de l'application
    """

    email_list = [{"email": "ok", "password": 123324234}, {"email": "fuck", "password": 321}, {"email": "joe", "password": 213}]
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Génère les éléments de la fenêtre.
        """
        layout = QVBoxLayout()
        central_widget = QWidget()

        self.email_scrollarea = QScrollArea()
        self.email_list_widget = QListWidget()
        self.email_list_widget.currentRowChanged.connect(self.test)
        self.email_list_widget.doubleClicked.connect(self.show_password)
        for email in self.email_list:
            item = QListWidgetItem()
            item.setText(f"{email.get("email")} \n"
                         f"{self.censor(str(email.get("password")))}")
            self.email_list_widget.addItem(item)

        self.email_scrollarea.setWidget(self.email_list_widget)
        self.email_scrollarea.setWidgetResizable(True)

        self.add_button = QPushButton("Ajouter")
        self.modify_button = QPushButton("Modifier")
        self.modify_button.setDisabled(True)
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setDisabled(True)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.modify_button)
        self.button_layout.addWidget(self.delete_button)

        layout.addWidget(self.email_scrollarea)
        layout.addLayout(self.button_layout)

        self.setMinimumSize(375, 220)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def enable_buttons(self):
        """
        Active les boutons qui ont besoins d'un objet sélectionné pour fonctionner
        """
        self.modify_button.setDisabled(False)
        self.delete_button.setDisabled(False)

        sender = self.sender()
        if isinstance(sender, QListWidget):
            print(sender.currentRow())

    def show_password(self):
        """
        Rend le mot de passe dans la rangée sélectionné visible pendant 3 secondes.
        """
        sender = self.sender()
        if isinstance(sender, QListWidget):
            item = sender.currentItem()
            email = self.email_list[sender.currentRow()]

            item.setText(f"{str(email.get("email"))} \n"
                         f"{str(email.get("password"))}")

            timer = QTimer()
            timer.singleShot(3000, lambda:
            item.setText(f"{email.get("email")} \n"
                         f"{self.censor(str(email.get("password")))}"))

    @staticmethod
    def censor(password):
        """
        Retourne une chaine de caractères sous forme d'astérix
        :param password: La chaine de caractère à censurer.
        :return: La chaine de caractère censurée.
        """
        censored_password = ""
        for char in password:
            censored_password += "*"
        return censored_password


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Page d'acceuil")
    window.show()
    sys.exit(app.exec())
