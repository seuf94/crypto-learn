def dire_bonjour() : 
    print(" Bonjour à tous ")

def saluer(prénom) :
    print(f"Salut, {prénom} ! ")

def carre(x) : 
    return x * x

if __name__ == "__main__": 
    dire_bonjour()

    prénom = input("Comment tu t'appelles ? ")
    saluer(prénom)

    n_str = input("Entrez un nombre")
    n = int(n_str)
    resultat = carre(n)
    print(f"Le carré de {n} est {resultat}.")