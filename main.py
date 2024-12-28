from blockchain import Blockchain
from transaction import Transaction
from crypto_util import generer_cle_privee, obtenir_cle_publique
from bloc import Bloc

def main():
    # Création d'un bloc initial pour illustration
    bloc_initial = Bloc(0, "Bloc initial", "0")
    print("\n--- Bloc initial ---")
    print("Index:", bloc_initial.index)
    print("Timestamp:", bloc_initial.timestamp)
    print("Données:", bloc_initial.donnees)
    print("Hash précédent:", bloc_initial.hash_precedent)
    print("Hash actuel:", bloc_initial.hash_actuel)

    # Génération des clés
    cle_privee = generer_cle_privee()
    cle_publique = obtenir_cle_publique(cle_privee)
    print("\n--- Clés générées ---")
    print("Clé privée:", cle_privee)
    print("Clé publique:", cle_publique)

    # Création de la blockchain
    blockchain = Blockchain()
    print("\n--- Blockchain créée ---")
    print("Bloc initial ajouté à la chaîne.")

    # Création d'une transaction
    transaction = Transaction("Alice", "Bob", 50, cle_privee)
    print("\n--- Transaction créée ---")
    print("Expéditeur:", transaction.expediteur)
    print("Destinataire:", transaction.destinataire)
    print("Montant:", transaction.montant)
    print("Signature:", transaction.signature)
    print("Hash de la transaction:", transaction.transaction_hash)

    # Validation et ajout de la transaction
    print("\n--- Validation de la transaction ---")
    if Transaction.verifier_transaction(transaction, cle_publique):
        print("Transaction valide.")
        blockchain.ajouter_bloc({"transaction": vars(transaction), "transaction_hash": transaction.transaction_hash})
        print("Transaction ajoutée au bloc.")
    else:
        print("Transaction invalide.")

    # Afficher l'état de la blockchain
    print("\n--- État de la Blockchain ---")
    for bloc in blockchain.chaine:
        print("\nBloc index:", bloc.index)
        print("Timestamp:", bloc.timestamp)
        print("Données:", bloc.donnees)
        print("Hash précédent:", bloc.hash_precedent)
        print("Hash actuel:", bloc.hash_actuel)

    # Vérification de l'intégrité de la blockchain
    print("\n--- Vérification de l'intégrité ---")
    if blockchain.verifier_integrite():
        print("La blockchain est intègre.")
    else:
        print("La blockchain a été compromise.")

if __name__ == "__main__":
    main()
