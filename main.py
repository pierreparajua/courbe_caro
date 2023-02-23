from classes_menu import MenuFolder, MenuFile, SimpleChoice, concat_choice, nbr_climb
from classes_ares import FileAresDeform, FileAresTempStd, FileAresTemp2climb, FileAresTempMulti
from classes_at import FileAtFreq, FileAtEcoul
from classes_metler import FileMetlerTempE, FileMetlerTempF
from utils import check_error_menu
from pathlib import Path

FICHIERS = Path(__file__).resolve().parent / "fichiers"

print("\t\t Bienvenue dans le traceur de courbe\t")

while True:
    # Affiche le menu de sélection des instruments
    choix_instrument = check_error_menu(MenuFolder, FICHIERS)
    if choix_instrument.answer != 0:
        path_instrument = choix_instrument.choices[choix_instrument.answer - 1]
        # Affiche le menu de sélection des techniques
        choix_technique = check_error_menu(MenuFolder, path_instrument)
        if choix_technique.answer != 0:
            path_technique = choix_technique.choices[choix_technique.answer - 1]
            # Affiche le menu de sélection des fichiers
            choix_fichier = check_error_menu(MenuFile, path_technique)
            if choix_fichier.answer != 0:
                file_name = choix_fichier.choices[choix_fichier.answer - 1]
                file_path = path_technique / Path(file_name)
                # Exécute la méthode "show_graph" en fonction des techniques
                print(path_technique.name)
                if path_technique.name == "ARESG2_balayage_deformation":
                    FileAresDeform(file_path, file_name).show_graph()
                if path_technique.name == "ARESG2_balayage_temperature":
                    dfs = [file_path]
                    f_names = [file_name]
                    # Permet la sélection de plusieurs fichiers
                    while SimpleChoice(concat_choice).answer == 1:
                        choix_fichier = MenuFile(path_technique)
                        file_name = choix_fichier.choices[choix_fichier.answer - 1]
                        file_path = path_technique / Path(file_name)
                        dfs.append(file_path)
                        f_names.append(file_name)
                    if len(dfs) == 1:
                        # Si 1 seul fichier : choix entre 2 montées ou std
                        if SimpleChoice(nbr_climb).answer == 2:
                            FileAresTempStd(file_path=dfs[0], title_graph=file_name).show_graph()
                        else:
                            FileAresTemp2climb(file_path=dfs[0], title_graph=file_name).show_graph()
                    else:
                        # Si 2 fichiers
                        file1_name = str(f_names[0][0:9])
                        file2_name = str(f_names[1][0:9])
                        title = file1_name + "/" + file2_name
                        FileAresTempMulti(files_path=dfs,
                                          title_graph=title,
                                          f_name1=file1_name,
                                          f_name2=file2_name).show_graph()

                if path_technique.name == "AT_balayage_deformation":
                    print("A faire ")
                if path_technique.name == "AT_balayage_temperature":
                    print("A faire ")
                if path_technique.name == "AT_balayge_frequence":
                    FileAtFreq(file_path=file_path, title_graph=file_name).show_graph()
                if path_technique.name == "AT_ecoulement":
                    x= FileAtEcoul(file_path=file_path, title_graph=file_name)
                    print(x.df)
                    FileAtEcoul(file_path=file_path, title_graph=file_name).show_graph()
                if path_technique.name == "Metler_balayage_temperature":
                    FileMetlerTempE(file_path=file_path, title_graph=file_name).show_graph()
                    FileMetlerTempF(file_path=file_path, title_graph=file_name).show_graph()


