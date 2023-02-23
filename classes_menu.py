from os import listdir
from os.path import isfile, join

concat_choice = "Souhaitez vous rajouter un deuxième fichier ?: \n1- oui\n2- non\n"
nbr_climb = "Souhaitez vous la deuxième montée ?: \n1- oui\n2- non\n"


class MenuFolder:
    # Classe qui permet ne naviguer dans des dossiers en affichant un menu de sélection
    def __init__(self, folder_path):
        self.folder_path: Path = folder_path
        self.choices: list = self.get_folders_list()
        self.answer: int = self.get_answer()

    def get_folders_list(self):
        return [d for d in self.folder_path.iterdir() if d.is_dir()]

    def display_folder_list(self):
        for choice in self.choices:
            print(f"{self.choices.index(choice) + 1} - {choice.name}")

    def get_answer(self):
        self.display_folder_list()
        answer = int(input("Choisissez : "))
        print("\n")
        return answer

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if value not in (range(0, len(self.choices) + 1)):
            raise ValueError("Le choix n'est pas correct")
        self._answer = value


class MenuFile:
    # Classe qui permet de sélectionner un fichier dans le dossier en paramètre
    def __init__(self, folder_path):
        self.file_path: Path = folder_path
        self.choices: list = self.get_files_list()
        self.answer: int = self.get_answer()

    def get_files_list(self):
        return [f for f in listdir(self.file_path) if isfile(join(self.file_path, f))]

    def display_file_list(self):
        for choice in self.choices:
            print(f"{self.choices.index(choice) + 1} - {choice}")
        print("\n")

    def get_answer(self):
        self.display_file_list()
        answer = int(input("Choisissez : "))
        return answer

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if value not in range(0, len(self.choices) + 1) or 0:
            raise ValueError("Le choix n'est pas correct")
        self._answer = value


class SimpleChoice:
    def __init__(self, question):
        self.question: str = question
        self.answer: int = self.get_answer()

    def get_answer(self):
        print(self.question)
        answer = int(input("Choisissez : "))
        return answer

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, value):
        if value not in [1, 2]:
            raise ValueError("Le choix n'est pas correct")
        self._answer = value
