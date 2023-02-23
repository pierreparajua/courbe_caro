
def check_error_menu(menu, path):
    while True:
        try:
            response = menu(path)
        except ValueError:
            print("Erreur dans le choix du menu")
        else:
            return response
