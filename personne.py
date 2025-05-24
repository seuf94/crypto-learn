# personne.py

class Personne:
    """Classe qui représente une personne avec nom et âge."""
    def __init__(self, nom, age):
        # Attributs définis à la création de l'objet
        self.nom = nom
        self.age = age

    def se_presenter(self):
        """Affiche le nom et l'âge de la personne."""
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

    def anniversaire(self):
        """Incrémente l'âge de la personne et affiche un message."""
        self.age += 1
        print(f"Joyeux anniversaire ! J'ai maintenant {self.age} ans.")
        self.age += 1 
        print(f"Joyeux anniversaire ! J'ai maintenant {self.age} ans.")

if __name__ == "__main__":
    # Création d'instances de Personne
    p1 = Personne("Sar", 27)
    p2 = Personne("Sam", 30)
    p3 = Personne("Nab", 25)

    # Appel des méthodes sur ces objets
    p1.se_presenter()
    p2.se_presenter()
    p3.se_presenter()

    # Fêter l'anniversaire de p1 deux fois pour voir l'évolution
    p1.anniversaire()
    p3.anniversaire()
