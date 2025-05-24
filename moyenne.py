saisie = input("Entre cinq nombres, séparés par des espaces : ")

liste_str = saisie.split()
nombres = [float(x) for x in liste_str]

total = sum(nombres)

print(f"Sum  = {total}")