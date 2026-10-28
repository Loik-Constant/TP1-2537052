import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QScrollArea, QWidget, QListWidget, \
    QListWidgetItem, QPushButton, QHBoxLayout, QFormLayout, QLineEdit
from PySide6.QtCore import QTimer, Signal

from app.core.storage import PasswordStorage
from app.ui.generator_ui import PasswordGeneratorUi


class EmailForm(QWidget):
    """
    Formulaire utilisé pour la création de nouvels emails.
    """
    email_submitted = Signal(object)

    def __init__(self, email: dict[str, str] | None = None):
        """
        Initialise une nouvelle instance de EmailForm.

        :param default_email: Les informations de l'e-mail présent dans le formulaire, utilisé lors de l'édition
        """
        super().__init__()
        self.email = email
        if self.email is not None:
            self.setWindowTitle("Formulaire d'édition d'email")
        else:
            self.setWindowTitle("Formulaire de création d'email")
        self.setup_ui()

    def setup_ui(self):
        """
        Génère les éléments de la fenêtre.
        """
        layout = QFormLayout()

        self.email_edit = QLineEdit()
        self.password_edit = QLineEdit()

        if self.email is not None:
            self.email_edit.setText(self.email.get("email"))
            self.password_edit.setText(self.email.get("password"))

        layout.addRow("E-mail :", self.email_edit)
        layout.addRow("Mot de passe :", self.password_edit)

        self.generate_button = QPushButton("Générer")
        self.submit_button = QPushButton("Soumettre")

        self.generate_button.clicked.connect(self.show_password_generator)
        self.submit_button.clicked.connect(self.submit_email)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.generate_button)
        self.button_layout.addWidget(self.submit_button)
        layout.addRow(self.button_layout)

        self.setLayout(layout)

    def submit_email(self):
        """
        Crée un nouvel email avec l'information du formulaire
        """
        email = {"email": self.email_edit.text(), "password": self.password_edit.text()}
        self.email_submitted.emit(email)
        self.close()


    def show_password_generator(self):
        """
        Affiche la fenêtre de génération de mot de passe.
        """
        self.password_generator = PasswordGeneratorUi()
        self.password_generator.show()



class MainWindow(QMainWindow):
    """
    Fenêtre principale de l'application
    """
    def __init__(self, vault_file: str):
        super().__init__()
        self.email_list = []
        self.passwordStorage = PasswordStorage(vault_file)
        self.setWindowTitle("Page d'acceuil")
        self.init_ui()

    def init_ui(self):
        """
        Génère les éléments de la fenêtre.
        """
        layout = QVBoxLayout()
        central_widget = QWidget()

        self.email_scrollarea = QScrollArea()
        self.email_list_widget = QListWidget()
        self.email_list_widget.itemClicked.connect(self.enable_buttons)
        self.email_list_widget.itemDoubleClicked.connect(self.show_password)
        for email in self.passwordStorage.read_vault_file():
            self.add_email(email)

        self.email_scrollarea.setWidget(self.email_list_widget)
        self.email_scrollarea.setWidgetResizable(True)

        self.add_button = QPushButton("Ajouter")
        self.modify_button = QPushButton("Modifier")
        self.modify_button.setDisabled(True)
        self.delete_button = QPushButton("Supprimer")
        self.delete_button.setDisabled(True)

        self.add_button.clicked.connect(self.show_create_form)
        self.modify_button.clicked.connect(self.show_edit_form)

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

        self.form.close()

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

    def show_create_form(self):
        """
        Affiche le formulaire de création d'e-mail.
        """
        self.form = EmailForm()
        self.form.email_submitted.connect(self.add_email)
        self.form.show()

    def show_edit_form(self):
        """
        Affiche le formulaire de modification d'e-mail.
        """
        self.form = EmailForm(self.email_list[self.email_list_widget.currentRow()])
        self.form.email_submitted.connect(self.edit_email)
        self.form.show()

    def add_email(self, email: dict[str, str]):
        self.email_list.append(email)

        item = QListWidgetItem()
        item.setText(f"{email.get("email")} \n"
                     f"{self.censor(str(email.get("password")))}")
        self.email_list_widget.addItem(item)

    def edit_email(self, email: dict[str, str]):
        self.email_list[self.email_list_widget.currentRow()] = email

        item = self.email_list_widget.currentItem()
        item.setText(f"{email.get("email")} \n"
                     f"{self.censor(str(email.get("password")))}")

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
    window = MainWindow("vault.json")
    window.show()
    sys.exit(app.exec())
