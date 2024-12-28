from bloc import Bloc

class Blockchain:
    def __init__(self):
        self.chaine = [self.creer_bloc_initial()]
        self.transactions_enregistrees = set()  # Stocke les hashes des transactions enregistrées

    def creer_bloc_initial(self):
        return Bloc(0, "Bloc initial", "0")

    def ajouter_bloc(self, donnees):
        dernier_bloc = self.chaine[-1]
        nouveau_bloc = Bloc(len(self.chaine), donnees, dernier_bloc.hash_actuel)
        
        # Vérifier si la transaction est déjà enregistrée
        transaction_hash = donnees.get("transaction_hash")
        if transaction_hash in self.transactions_enregistrees:
            raise ValueError("La transaction a déjà été enregistrée (attaque par rejeu détectée)")

        # Ajouter la transaction dans la liste des transactions enregistrées
        self.transactions_enregistrees.add(transaction_hash)
        self.chaine.append(nouveau_bloc)

    def verifier_integrite(self):
        for i in range(1, len(self.chaine)):
            bloc_actuel = self.chaine[i]
            bloc_precedent = self.chaine[i - 1]
            if bloc_actuel.hash_precedent != bloc_precedent.hash_actuel:
                return False
            if bloc_actuel.hash_actuel != bloc_actuel.calculer_hash():
                return False
        return True
