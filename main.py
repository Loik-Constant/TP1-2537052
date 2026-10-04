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

    passwordGenerator = PasswordGenerator(args.length, args.no_lower, args.no_upper, args.no_digits, args.no_symbols, args.validate)
    password = passwordGenerator.generate_password()

    if password == -1:
        print("ERREUR: Vous devez spécifier au moins un type de caractère valide")
    elif password == -2:
        print("ERREUR: La longueur est trop courte pour générer un mot de passe contenant chaque types de caractère spécifié")
    else:
        print("Mot de passe généré: " + password)


if __name__ == "__main__":
    main()