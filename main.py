# Loïk Constant, 2537052, Loik-Constant

import argparse
import sys

from PySide6.QtWidgets import QApplication

from app.core.generator import PasswordGenerator
from app.ui.main_window import MainWindow


def main():
    parser = argparse.ArgumentParser(description="Générateur de mots de passe CLI")

    parser.add_argument("-l", "--length", type=int, default=16, help="La longueur du mot de passe généré")

    parser.add_argument("-nl", "--no-lower", action="store_true",
                        help="Empêche le mot de passe de contenir des lettres minuscules")

    parser.add_argument("-nu", "--no-upper", action="store_true",
                        help="Empêche le mot de passe de contenir des lettres majuscules")

    parser.add_argument("-nd", "--no-digits", action="store_true",
                        help="Empêche le mot de passe de contenir des chiffres")

    parser.add_argument("-ns", "--no-symbols", action="store_true",
                        help="Empêche le mot de passe de contenir des symboles spéciaux")

    parser.add_argument("-v", "--validate", action="store_true",
                        help="Garantie que le mot de passe contiendra au moins un caractère de chaque type spécifié")

    parser.add_argument("-ng", "--no-gui", action="store_true",
                        help="Lance l'application sans interface graphique")

    parser.add_argument("-vf", "--vault-file", type=str, default="vault.json", help="Le fichier .json dans lequel les données seront lues et enregistrées")


    args = parser.parse_args()

    if args.no_gui:
        password_generator = PasswordGenerator(args.length, args.no_lower, args.no_upper, args.no_digits, args.no_symbols, args.validate)
        try:
            print(password_generator.generate_password())
        except ValueError as e:
            print(f"Erreur : {e}")
    else:
        app = QApplication(sys.argv)
        window = MainWindow("vault.json")
        window.show()
        sys.exit(app.exec())



if __name__ == "__main__":
    main()