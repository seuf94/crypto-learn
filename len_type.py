# len_type.py

# 1) On demande un mot à l'utilisateur
mot = input("Tape un mot de ton choix : ")

# 2) On calcule sa longueur avec len()
longueur = len(mot)

# 3) On affiche la longueur et le type de la variable mot
print(f"Ton mot « {mot} » contient {longueur} caractères.")
print(f"Le type de la variable 'mot' est {type(mot)}.")
