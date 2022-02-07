from src.util.util import hash256


class BlockHeader:
    """
    Block Header is the block meta-data container
    """

    def __init__(self, version, previous_hash, merkle_root, timestamp, bits):
        self.version = version
        self.previous_hash = previous_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.hash = ''

    def mine(self):
        while self.hash[0:4] != '0000':
            self.hash = hash256((
                str(self.version) +
                self.previous_hash +
                self.merkle_root +
                str(self.timestamp) +
                str(self.bits) +
                str(self.nonce)
            ).encode()).hex()

            self.nonce += 1
            print(f"Mining started {self.nonce}", end='\r')
