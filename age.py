# age.py

# 1. On demande l'âge à l'utilisateur
age_str = input("Quel âge as-tu ? ")

# 2. On convertit la saisie (chaîne) en entier
age = int(age_str)

# 3. On vérifie si l'utilisateur est majeur ou mineur
if age >= 18:
    print("Tu es majeur·e ! 🎉")
else:
    print("Tu es mineur·e. Patience, la majorité arrive bientôt ! 😊")
