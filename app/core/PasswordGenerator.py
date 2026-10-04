from random import randint


class PasswordGenerator:
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["#", "\\", "~", "|", "!", "\"", "@", "/", "$", "%", "?", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "<", ">", ":", ";", "^", "'", "`", ".", ","]

    def __init__(self, length, has_lower, has_upper, has_digits, has_symbols, validation):
        self.length = length
        self.has_lower = has_lower
        self.has_upper = has_upper
        self.has_digits = has_digits
        self.has_symbols = has_symbols
        self.validation = validation

    def generate_password(self):
        valid_characters = []
        category_amount = 0
        if self.has_lower:
            [valid_characters.append(x) for x in PasswordGenerator.lower_letters]
            category_amount += 1
        if self.has_upper:
            [valid_characters.append(x) for x in PasswordGenerator.upper_letters]
            category_amount += 1
        if self.has_digits:
            [valid_characters.append(x) for x in PasswordGenerator.digits]
            category_amount += 1
        if self.has_symbols:
            [valid_characters.append(x) for x in PasswordGenerator.symbols]
            category_amount += 1
        if self.length < category_amount:
            self.validation = False

        password = ""
        valid = False
        while not valid:
            while len(password) < self.length:
                password += valid_characters[randint(0, len(valid_characters) - 1)]

            if self.validation:
                if self.password_is_valid(password):
                    valid = True
                else:
                    password = ""
            else:
                valid = True

        return password

    def password_is_valid(self, password):
        if (self.has_lower and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.lower_letters)):
            return False
        if (self.has_upper and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.upper_letters)):
            return False
        if (self.has_digits and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.digits)):
            return False
        if (self.has_symbols and
            not PasswordGenerator.password_has_character_type(password, PasswordGenerator.symbols)):
            return False
        return True

    @staticmethod
    def password_has_character_type(password, character_list):
        for character1 in password:
            for character2 in character_list:
                if character1 == character2:
                    return True
        return False

test = PasswordGenerator(3, True, True, True, True, True)
print(test.generate_password())