from statistics import mean

username = []
usernote = []

for i in range(5):
    name = input("Entrer le nom de l'étudiant {} : ".format(i + 1))

    note = int(input("Entrer la note de l'étudiant {} : ".format(i + 1)))
    while note < 0 or note > 20:
        print("Note invalide. Entrez une note entre 0 et 20.")
        note = int(input("Entrer la note de l'étudiant {} : ".format(i + 1)))

    username.append(name)
    usernote.append(note)

moyenne = mean(usernote)

print("Résultats :")
for i in range(5):
    resultat = ("Réussi", "Échoué")[usernote[i] < 10]  # "<" au lieu de "<="
    print(f"{username[i]} : {usernote[i]} - {resultat}")

print(f"La moyenne de la classe est : {moyenne}")
