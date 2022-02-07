import hashlib
import random


def hash256(string):
    """Creates two round solve of hash 256"""
    return hashlib.sha256(hashlib.sha256(string).digest()).digest()

def random_bits():
    bits = [''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    return bits[0]