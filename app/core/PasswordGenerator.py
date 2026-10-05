# Loïk Constant, 2537052, Loik-Constant

from random import randint


class PasswordGenerator:
    """
    Permet de générer des mots de passe selon différents critères.
    """
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["#", "\\", "~", "|", "!", "\"", "@", "/", "$", "%", "?", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "<", ">", ":", ";", "^", "'", "`", ".", ","]

    def __init__(self, length: int, no_lower: bool, no_upper: bool, no_digits: bool, no_symbols: bool, validate: bool):
        """
        Initialise une instance de PasswordGenerator.

        :param length: La longueur des mots de passe générés.
        :param no_lower: Empêche les mots de passe de contenir des lettres minuscules.
        :param no_upper: Empêche les mots de passe de contenir des lettres majuscules.
        :param no_digits: Empêche les mots de passe de contenir des chiffres.
        :param no_symbols: Empêche les mots de passe de contenir des symboles spéciaux.
        :param validate: Garantie que les mots de passe contiendront au moins un caractère de chaque type spécifié.
        """
        self.length = length
        self.no_lower = no_lower
        self.no_upper = no_upper
        self.no_digits = no_digits
        self.no_symbols = no_symbols
        self.validate = validate

    def generate_password(self) -> str:
        """
        Génère un mot de passe selon les critères spécifié.

        :return: Le mot de passe généré.
        """
        valid_characters = []
        category_amount = 0
        if not self.no_lower:
            [valid_characters.append(x) for x in PasswordGenerator.lower_letters]
            category_amount += 1
        if not self.no_upper:
            [valid_characters.append(x) for x in PasswordGenerator.upper_letters]
            category_amount += 1
        if not self.no_digits:
            [valid_characters.append(x) for x in PasswordGenerator.digits]
            category_amount += 1
        if not self.no_symbols:
            [valid_characters.append(x) for x in PasswordGenerator.symbols]
            category_amount += 1

        if self.length <= 0:
            raise ValueError("La longueur doit être plus grande que 0")
        if category_amount == 0:
            raise ValueError("Il doit y avoir au moins un type de caractère sélectionné")
        if self.length < category_amount and self.validate:
            raise ValueError("La longueur est trop courte pour générer un mot de passe contenant chaque type de caractère spécifié")

        password = ""
        valid = False
        while not valid:
            while len(password) < self.length:
                password += valid_characters[randint(0, len(valid_characters) - 1)]

            if self.validate:
                if self.password_is_valid(password):
                    valid = True
                else:
                    password = ""
            else:
                valid = True

        return password

    def password_is_valid(self, password: str) -> bool:
        """
        Vérifie si un mot de passe contient au moins un caractère de chaque type spécifié.

        :param password: Le mot de passe à vérifier.
        :return: True si le mot de passe est valide
        """
        if (not self.no_lower and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.lower_letters)):
            return False
        if (not self.no_upper and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.upper_letters)):
            return False
        if (not self.no_digits and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.digits)):
            return False
        if (not self.no_symbols and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.symbols)):
            return False
        return True

    @staticmethod
    def password_has_character_type(password: str, character_list: list[str]) -> bool:
        """
        Vérifie si un mot de passe contient un moins un caractère contenu dans la liste spécifiée.

        :param password: Le mot de passe à vérifier.
        :param character_list: La liste de caractères à comparer.
        :return: True si le mot de passe contient un caractère contenu dans la liste.
        """
        for character1 in password:
            for character2 in character_list:
                if character1 == character2:
                    return True
        return False