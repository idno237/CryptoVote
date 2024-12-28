from crypto_util import signer_donnees, verifier_signature
from hash_util import calculer_hash

class Transaction:
    def __init__(self, expediteur, destinataire, montant, cle_privee):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.montant = montant
        self.signature = self.signer_transaction(cle_privee)
        self.transaction_hash = self.calculer_hash_transaction()

    def signer_transaction(self, cle_privee):
        donnees = f"{self.expediteur}{self.destinataire}{self.montant}"
        return signer_donnees(cle_privee, donnees)

    def calculer_hash_transaction(self):
        """
        Calcule un hash unique pour la transaction.
        """
        donnees = f"{self.expediteur}{self.destinataire}{self.montant}{self.signature}"
        return calculer_hash(donnees)

    @staticmethod
    def verifier_transaction(transaction, cle_publique):
        donnees = f"{transaction.expediteur}{transaction.destinataire}{transaction.montant}"
        if not verifier_signature(cle_publique, donnees, transaction.signature):
            return False
        return True
