import csv


def fn_question(question):
    return input(question)


def fn_encode(nom, prenom, age):
    file_csv = "formulaire_majorite.csv"
    header = ["nom", "prenom", "age"]
    data = [nom, prenom, age]
    with open(file_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


q_nom = "Entrez votre nom : "
r_nom = fn_question(q_nom)
q_prenom = "Entrez votre prenom : "
r_prenom = fn_question(q_prenom)
q_age = "Entrez votre age : "
r_age = int(fn_question(q_age))

fn_encode(r_nom, r_prenom, r_age)

if r_age >= 18:
    print(r_prenom, r_nom, "est majeur")
else:
    print(r_prenom, r_nom, "est mineur")
