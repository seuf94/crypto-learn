# quiz.py

# 1) Initialisation du compteur de bonnes réponses
score = 0

# 2) Question 1
reponse = input("1) Quel langage utilises-tu pour ce quiz ? ")
if reponse.lower() == "python":
    score += 1  # on ajoute 1 si la réponse est correcte

# 3) Question 2
reponse = input("2) Quelle fonction sert à afficher du texte ? ")
if reponse.lower() in ["print", "print()"]:
    score += 1

# 4) Question 3
reponse = input("3) Quel mot-clé crée une boucle en Python ? ")
if reponse.lower() == "for":
    score += 1

# 5) Affichage du résultat
print(f"Ton score est {score} sur 3.")
