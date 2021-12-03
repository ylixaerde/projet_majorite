import csv
import os
from os import path
import glob


def fn_file_to_open():
    path = os.path.realpath(__file__)
    work_dir = os.path.dirname(path)
    search_ext = '.csv'
    csv_files = glob.glob(f'{work_dir}\*{search_ext}')
    print(f'\nFichier CSV présent dans le dossier')
    x = 0
    for file in csv_files:
        x += 1
        file_name = os.path.basename(file)
        print(f'[{x}] {file_name}')
    liste_num = list(range(len(csv_files)))
    liste_num = [i + 1 for i in liste_num]
    status = 0
    x = 1
    while status not in liste_num:
        q_status = "Entrer votre choix : "
        e_status = "\nErreur : Choix non-valide\n"
        if x != 1:
            print(e_status)
        status = input(q_status)
        try:
            status = int(status)
        except ValueError:
            debug = "Caractère invalide"
        x += 1
    status -= 1
    return os.path.basename(csv_files[status])


def fn_question(question, erreur):
    reponse = input(question)
    while not reponse.isalpha():
        print(erreur)
        reponse = input(question)
    return reponse


def fn_question_int(question, erreur):
    reponse = input(question)
    while not reponse.isnumeric():
        print(erreur)
        reponse = input(question)
    return reponse


def fn_is_majeur(age):
    if int(age) >= 18:
        return True
    else:
        return False


def fn_encode(file_csv, nom, prenom, age):
    if path.exists(file_csv):
        data = [nom, prenom, age]
        with open(file_csv, "a", encoding="utf-8", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(data)
        print(f'{prenom} {nom}, age : {age} ans, a été encodé')
    else:
        header = ["nom", "prenom", "age"]
        s = ", "
        header_str = s.join(header)
        data = [nom, prenom, age]
        with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(header)
            writer.writerow(data)
        print(f'En-tête du fichier CSV encodée : {header_str}')
        print(f'{prenom} {nom}, age : {age} ans, a été encodé')


def fn_formulaire(file_csv):
    q_nom = "Entrez votre nom : "
    e_nom = "\nErreur : Caractères invalides\n"
    r_nom = fn_question(q_nom, e_nom)
    q_prenom = "Entrez votre prenom : "
    e_prenom = "\nErreur : Caractères invalides\n"
    r_prenom = fn_question(q_prenom, e_prenom)
    q_age = "Entrez votre age : "
    e_age = "\nErreur : Caractères invalides\n"
    r_age = fn_question_int(q_age, e_age)
    fn_encode(file_csv, r_nom, r_prenom, r_age)


def fn_list_user(file_csv):
    if path.exists(file_csv):
        with open(file_csv, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            print(f'\nListe des utilisateurs :')
            x = 0
            for line in reader:
                r_nom = line[0]
                r_prenom = line[1]
                r_age = line[2]
                if r_age.isnumeric():
                    x += 1
                    if fn_is_majeur(r_age):
                        print(f'{x}. {r_prenom} {r_nom} est majeur')
                    else:
                        print(f'{x}. {r_prenom} {r_nom} est mineur')
            print('')
            input(f'Appuyer sur entrée pour continuer')
    else:
        print(f'\nErreur : Fichier introuvable\n')


def fn_list_majeur(file_csv):
    if path.exists(file_csv):
        with open(file_csv, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            print(f'\nListe des utilisateurs majeurs :')
            x = 0
            for line in reader:
                r_nom = line[0]
                r_prenom = line[1]
                r_age = line[2]
                if r_age.isnumeric() and fn_is_majeur(r_age):
                    x += 1
                    print(f'{x}. {r_prenom} {r_nom} est majeur')
            print('')
            input(f'Appuyer sur entrée pour continuer')
    else:
        print(f'\nErreur : Fichier introuvable\n')


def fn_list_mineur(file_csv):
    if path.exists(file_csv):
        with open(file_csv, "r", encoding="utf-8") as fichier:
            reader = csv.reader(fichier)
            print(f'\nListe des utilisateurs mineurs :')
            x = 0
            for line in reader:
                r_nom = line[0]
                r_prenom = line[1]
                r_age = line[2]
                if r_age.isnumeric() and not fn_is_majeur(r_age):
                    x += 1
                    print(f'{x}. {r_prenom} {r_nom} est mineur')
            print('')
            input(f'Appuyer sur entrée pour continuer')
    else:
        print(f'\nErreur : Fichier introuvable\n')


def fn_init_menu():
    q_choix_1 = "[1] Encoder un utilisateur"
    q_choix_2 = "[2] Afficher la liste des utilisateurs encodés"
    q_choix_3 = "[3] Afficher les utilisateurs majeurs"
    q_choix_4 = "[4] Afficher les utilisateurs mineurs"
    q_choix_5 = "[5] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4, q_choix_5]
    return list_menu


def fn_menu(list_menu, file_csv):
    print(f'\n----Menu - Projet Majorité----')
    for item in list_menu:
        print(f'{item}')
    q_status = "Entrer votre choix (1-5) : "
    e_status = "\nErreur : Caractères invalides\n"
    status = int(fn_question_int(q_status, e_status))
    match status:
        case 1:
            fn_formulaire(file_csv)
            return True
        case 2:
            fn_list_user(file_csv)
            return True
        case 3:
            fn_list_majeur(file_csv)
            return True
        case 4:
            fn_list_mineur(file_csv)
            return True
        case 5:
            print(f'Fermeture de l\'application')
            return False
        case _:
            print(f'\nErreur : Choix non-valide\n')
            return True


def fn_app():
    boucle = True
    file_csv = fn_file_to_open()
    list_menu = fn_init_menu()
    while boucle:
        boucle = fn_menu(list_menu, file_csv)


fn_app()
