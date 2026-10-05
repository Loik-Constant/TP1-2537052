# Loïk Constant, 2537052, Loik-Constant

import argparse

from app.core.PasswordGenerator import PasswordGenerator


def main():
    parser = argparse.ArgumentParser(description="Générateur de mots de passe CLI")

    parser.add_argument("-l", "--length", type=int, default=16, help="Longueur du mot de passe généré")

    parser.add_argument("-nl", "--no-lower", action="store_true",
                        help="Empêche le mot de passe de contenir des lettres minuscules")

    parser.add_argument("-nu", "--no-upper", action="store_true",
                        help="Empêche le mot de passe de contenir des lettres majuscules")

    parser.add_argument("-nd", "--no-digits", action="store_true",
                        help="Empêche le mot de passe de contenir des chiffres")

    parser.add_argument("-ns", "--no-symbols", action="store_true",
                        help="Empêche le mot de passe de contenir des symboles spéciales")

    parser.add_argument("-v", "--validate", action="store_true",
                        help="Garantie que le mot de passe contiendra au moins un caractère de chaque type spécifié")

    args = parser.parse_args()

    password_generator = PasswordGenerator(args.length, args.no_lower, args.no_upper, args.no_digits, args.no_symbols, args.validate)
    try:
        print(password_generator.generate_password())
    except ValueError as e:
        print(f"Erreur : {e}")



if __name__ == "__main__":
    main()