import json
from json import JSONDecodeError
from plistlib import InvalidFileException


class PasswordStorage:
    def __init__(self, vault_file="vault.json"):#"vault.json"):
        """
        Initialise une instance de PasswordStorage.

        :param vault_file: Le fichier .json dans lequel les données seront lues et enregistrées.
        """
        self.vault_file = vault_file
        self.create_vault_file()

    def create_vault_file(self):
        """
        Crée le fichier coffre-fort s'il n'existe pas déja
        """
        try:
            with open(self.vault_file, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
        except FileNotFoundError:
            print(f"Erreur: Le fichier {self.vault_file} n'as pas pu être crée")

    def save_vault_file(self, emails: list[dict[str, str]]):
        """
        Enregistre une liste d'e-mails dans le fichier coffre-fort.

        :param emails: La liste d'e-mails à enregistrer
        """
        try:
            with open(self.vault_file, "w", encoding="utf-8") as file:
                json.dump(emails, file, indent=4)
        except FileNotFoundError:
            print(f"Erreur: Le fichier {self.vault_file} n'as pas pu être crée")

    def read_vault_file(self):
        try:
            with open(self.vault_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Erreur: Le fichier {self.vault_file} n'existe pas")
            raise
        except InvalidFileException:
            print(f"Erreur: Le fichier {self.vault_file} n'est pas un fichier .json")
            raise