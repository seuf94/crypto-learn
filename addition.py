# addition.py

# 1) On demande deux nombres à l’utilisateur
n1_str = input("Entrez le premier nombre : ")
n2_str = input("Entrez le deuxième nombre : ")

# 2) Conversion en entier
n1 = int(n1_str)
n2 = int(n2_str)

# 3) Calcul de la somme
somme = n1 + n2

# 4) Affichage du résultat
print(f"La somme de {n1} et {n2} est {somme}.")
