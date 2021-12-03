import csv

nom = fn_question(question_nom)

def fn_encode(nom, prenom, age):
    file_csv = "formulaire_majorite.csv"
    header = ["nom", "prenom", "age"]
    data = [nom, prenom, age]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)
