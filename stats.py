# stats.py

# 1) On demande plusieurs nombres séparés par des espaces
saisie = input("Entre cinq nombres, séparés par des espaces : ")

# 2) On découpe la chaîne en morceaux, on convertit chacun en int
liste_str = saisie.split()            # ex. ["10", "5", "42", "3", "17"]
nombres = [int(x) for x in liste_str] # ex. [10, 5, 42, 3, 17]

# 3) On utilise les fonctions utilitaires
maximum = max(nombres)
minimum = min(nombres)
total   = sum(nombres)
trié    = sorted(nombres)

# 4) On affiche les résultats
print(f"Nombres : {nombres}")
print(f"Max  = {maximum}")
print(f"Min  = {minimum}")
print(f"Sum  = {total}")
print(f"Sorted : {trié}")
