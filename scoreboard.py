# scoreboard.py

# 1) On demande combien de joueurs
count_str = input("Combien de joueurs veux-tu enregistrer ? ")
count = int(count_str)

# 2) On collecte les noms et scores
scores = {}  # dictionnaire nom → score
for i in range(1, count + 1):
    name = input(f"Nom du joueur #{i} : ")
    score_str = input(f"Score de {name} : ")
    score = int(score_str)
    scores[name] = score

# 3) Calculs
all_scores = list(scores.values())
total      = sum(all_scores)
average    = total / len(all_scores)
best_name  = max(scores, key=scores.get)
worst_name = min(scores, key=scores.get)
ranking    = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# 4) Affichage
print("\n--- Carnet de scores ---")
print(f"Total des points    : {total}")
print(f"Score moyen         : {average:.2f}")
print(f"Meilleur joueur     : {best_name} ({scores[best_name]})")
print(f"Pire performance    : {worst_name} ({scores[worst_name]})")
print("\nClassement général :")
for rank, (player, pts) in enumerate(ranking, start=1):
    print(f"{rank}. {player} – {pts} pts")
