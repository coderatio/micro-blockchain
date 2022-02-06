import hashlib


def hash256(string):
    """Creates two round solve of hash 256"""
    return hashlib.sha256(hashlib.sha256(string).digest()).digest()
