from blockchain import Blockchain
from transaction import Transaction
from crypto_util import generer_cle_privee, obtenir_cle_publique, signer_donnees, verifier_signature

def tester_hachage():
    blockchain = Blockchain()
    bloc = blockchain.chaine[0]
    assert bloc.hash_actuel == bloc.calculer_hash(), "Erreur : Le hash du bloc est invalide"
    print("Test de hachage : OK")

def tester_signature():
    message = "Données de la transaction"
    cle_privee = generer_cle_privee()
    cle_publique = obtenir_cle_publique(cle_privee)
    signature = signer_donnees(cle_privee, message)
    assert verifier_signature(cle_publique, message, signature), "Erreur : La signature est invalide"
    print("Test de signature : OK")

def tester_transaction_rejeu():
    blockchain = Blockchain()
    cle_privee = generer_cle_privee()
    transaction = Transaction("Alice", "Bob", 50, cle_privee)
    
    # Ajouter la transaction pour la première fois
    blockchain.ajouter_bloc({"transaction_hash": transaction.transaction_hash})
    
    try:
        # Ajouter la même transaction une seconde fois
        blockchain.ajouter_bloc({"transaction_hash": transaction.transaction_hash})
        assert False, "Erreur : Une attaque par rejeu n'a pas été détectée"
    except ValueError:
        print("Test de prévention de rejeu : OK")

def tester_transaction_non_signee():
    cle_privee = generer_cle_privee()
    cle_publique = obtenir_cle_publique(cle_privee)
    
    # Créer une transaction non signée (en manipulant directement les attributs)
    transaction = Transaction("Alice", "Bob", 50, cle_privee)
    transaction.signature = None  # Supprimer la signature
    
    assert not Transaction.verifier_transaction(transaction, cle_publique), "Erreur : Une transaction non signée a été acceptée"
    print("Test de transaction non signée : OK")

def run_tests():
    tester_hachage()
    tester_signature()
    tester_transaction_rejeu()
    tester_transaction_non_signee()

if __name__ == "__main__":
    run_tests()
