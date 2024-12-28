import hashlib

def calculer_hash(data):
    """
    Fonction pour calculer le hash SHA-256 d'une donnée.
    :param data: str, les données à hasher.
    :return: str, le hash SHA-256 sous forme de chaîne hexadécimale.
    """
    data_bytes = data.encode('utf-8')
    hash_object = hashlib.sha256(data_bytes)
    return hash_object.hexdigest()