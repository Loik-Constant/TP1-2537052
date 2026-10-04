# Loïk Constant, 2537052, Loik-Constant

from random import randint


class PasswordGenerator:
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["#", "\\", "~", "|", "!", "\"", "@", "/", "$", "%", "?", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "<", ">", ":", ";", "^", "'", "`", ".", ","]

    def __init__(self, length, no_lower, no_upper, no_digits, no_symbols, validate):
        self.length = length
        self.no_lower = no_lower
        self.no_upper = no_upper
        self.no_digits = no_digits
        self.no_symbols = no_symbols
        self.validate = validate

    # Génère un mot de passe selon les caractéristiques spécifié et le retourne.
    # Si aucun type de caractère n'est permis, retourne -1
    # Si le nombre de types de caractère différents est plus grand que la longueur du mot de passe, retourne -2
    def generate_password(self):
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

        if category_amount == 0:
            return -1
        if self.length < category_amount:
            return -2

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

    # Vérifie si le mot de passe contient au moins un caractère de chaque type de caractère demandé
    def password_is_valid(self, password):
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

    # Vérifie si le mot de passe contient au moins un caractère contenu dans la liste de caractères.
    @staticmethod
    def password_has_character_type(password, character_list):
        for character1 in password:
            for character2 in character_list:
                if character1 == character2:
                    return True
        return False

test = PasswordGenerator(0, False, False, False, True, True)
print(test.generate_password())