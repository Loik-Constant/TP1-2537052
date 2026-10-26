import sys

from PySide6.QtWidgets import QApplication, QWidget, QSlider, QSpinBox, QFormLayout, QCheckBox, QLabel, QLineEdit, \
    QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

from app.core.PasswordGenerator import PasswordGenerator


class PasswordGeneratorUi(QWidget):
    """
    Fenêtre permêttant de générer des mots de passe.
    """
    password = ""
    password_is_hidden = False

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Génère les éléments de la fenêtre.
        """
        layout = QFormLayout()

        self.length_spin = QSpinBox()
        self.length_spin.setRange(4, 50)
        self.length_spin.setValue(16)

        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setRange(4, 50)
        self.length_slider.setValue(16)

        self.length_spin.valueChanged.connect(self.update_length_controls)
        self.length_slider.valueChanged.connect(self.update_length_controls)

        self.lowercase_checkbox = QCheckBox("Lettres minuscules")
        self.lowercase_checkbox.setChecked(True)
        self.uppercase_checkbox = QCheckBox("Lettres majuscules")
        self.uppercase_checkbox.setChecked(True)
        self.digit_checkbox = QCheckBox("Chiffres")
        self.digit_checkbox.setChecked(True)
        self.symbol_checkbox = QCheckBox("Symboles")
        self.symbol_checkbox.setChecked(True)

        self.lowercase_checkbox.toggled.connect(self.update_character_type_controls)
        self.uppercase_checkbox.toggled.connect(self.update_character_type_controls)
        self.digit_checkbox.toggled.connect(self.update_character_type_controls)
        self.symbol_checkbox.toggled.connect(self.update_character_type_controls)

        self.upper_lower_layout = QHBoxLayout()
        self.upper_lower_layout.addWidget(self.lowercase_checkbox)
        self.upper_lower_layout.addWidget(self.uppercase_checkbox)

        self.digit_symbol_layout = QHBoxLayout()
        self.digit_symbol_layout.addWidget(self.digit_checkbox)
        self.digit_symbol_layout.addWidget(self.symbol_checkbox)

        self.password_label = QLineEdit()
        self.password_label.setReadOnly(True)
        self.password_label.setStyleSheet("font-size: 16px;")
        self.password_label.setPlaceholderText("Appuyer sur 'Générer'")

        self.generate_button = QPushButton("Générer")
        self.hide_button = QPushButton("Masquer")
        self.hide_button.setDisabled(True)
        self.copy_button = QPushButton("Copier")
        self.copy_button.setDisabled(True)

        self.generate_button.clicked.connect(self.generate_password)
        self.hide_button.clicked.connect(self.switch_password_visibility)
        self.copy_button.clicked.connect(self.copy_password)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.generate_button)
        self.button_layout.addWidget(self.hide_button)
        self.button_layout.addWidget(self.copy_button)

        layout.addRow("Longueur : ", self.length_spin)
        layout.addRow(self.length_slider)
        layout.addRow(QLabel("Types de caractères : "))
        layout.addRow(self.upper_lower_layout)
        layout.addRow(self.digit_symbol_layout)
        layout.addRow(self.password_label)
        layout.addRow(self.button_layout)


        self.setFixedSize(375, 220)
        self.setLayout(layout)


    def update_length_controls(self, value):
        """
        Synchronise la valeur des boutons incrémentaux et du slider de longueur.

        :param value: Nouvelle valeur de longueur
        """
        sender = self.sender()

        if isinstance(sender, QSlider):
            widget = self.length_spin
        else:
            widget = self.length_slider

        widget.blockSignals(True)
        widget.setValue(value)
        widget.blockSignals(False)

    def update_character_type_controls(self):
        """
        S'assure qu'il y a au moins un type de caractères sélectionné et que la longueur minimum du mot de passe
        n'est pas plus petit que le nombre de types de caractères.
        """
        sender = self.sender()
        amount_checked = self.get_amount_checked()

        if isinstance(sender, QCheckBox) and amount_checked == 0:
            sender.blockSignals(True)
            sender.setChecked(True)
            sender.blockSignals(False)

        self.length_spin.setMinimum(max(amount_checked, 1))
        self.length_slider.setMinimum(max(amount_checked, 1))

    def get_amount_checked(self):
        """
        Retourne le nombre de checkbox sélectionné.

        :returns: Le nombre de catégories sélectionné.
        """
        amount_checked = 0
        if self.lowercase_checkbox.isChecked():
            amount_checked += 1
        if self.uppercase_checkbox.isChecked():
            amount_checked += 1
        if self.digit_checkbox.isChecked():
            amount_checked += 1
        if self.symbol_checkbox.isChecked():
            amount_checked += 1
        return amount_checked

    def generate_password(self):
        """
        Génère un mot de passe selon les critères sélectionné est update le label s'il n'est pas caché.
        """
        self.hide_button.setDisabled(False)
        self.copy_button.setDisabled(False)

        passwordGenerator = PasswordGenerator(
            self.length_spin.value(),
            not self.lowercase_checkbox.isChecked(),
            not self.uppercase_checkbox.isChecked(),
            not self.digit_checkbox.isChecked(),
            not self.symbol_checkbox.isChecked(),
            True
        )

        self.password = passwordGenerator.generate_password()
        if not self.password_is_hidden:
            self.password_label.setText(self.password)

    def switch_password_visibility(self):
        """
        Rend le mot de passe invisible s'il est visible et vice-versa.
        """
        if self.password_is_hidden:
            self.password_label.setText(self.password)
            self.password_is_hidden = False
            self.hide_button.setText("Masquer")
        else:
            self.password_label.setText("")
            [self.password_label.setText(self.password_label.text() + "*") for x in self.password]
            self.password_is_hidden = True
            self.hide_button.setText("Afficher")

    def copy_password(self):
        """
        Copie le mot de passe dans le presse-papier.
        """
        QApplication.clipboard().setText(self.password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorUi()
    window.setWindowTitle("Générateur de mot de passe")
    window.show()
    sys.exit(app.exec())
