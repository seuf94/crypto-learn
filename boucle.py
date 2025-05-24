# boucle.py

# 1) On demande à l’utilisateur combien de fois répéter
n_str = input("Jusqu'à quel nombre veux-tu compter ? ")
n = int(n_str)

# 2) Boucle for pour afficher de 1 à n
for i in range(1, n+1):
    print(i)
