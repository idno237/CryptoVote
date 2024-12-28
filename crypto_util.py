from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def generer_cle_privee():
    """
    Génère une clé privée RSA.
    """
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

def obtenir_cle_publique(cle_privee):
    """
    Extrait la clé publique à partir d'une clé privée.
    """
    return cle_privee.public_key()

def signer_donnees(cle_privee, donnees):
    """
    Signe les données avec une clé privée.
    """
    signature = cle_privee.sign(
        donnees.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verifier_signature(cle_publique, donnees, signature):
    """
    Vérifie si une signature est valide.
    """
    try:
        cle_publique.verify(
            signature,
            donnees.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False