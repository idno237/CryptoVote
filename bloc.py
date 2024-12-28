import time
from hash_util import calculer_hash  # Import de la fonction de hachage

class Bloc:
    def __init__(self, index, donnees, hash_precedent):
        self.index = index
        self.timestamp = time.time()
        self.donnees = donnees
        self.hash_precedent = hash_precedent
        self.hash_actuel = self.calculer_hash()

    def calculer_hash(self):
        contenu = f"{self.index}{self.timestamp}{self.donnees}{self.hash_precedent}"
        return calculer_hash(contenu)