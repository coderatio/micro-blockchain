# import sys

# sys.path.append('/full_path_to_project_parent_folder e.g /Users/josiah/Projects/Bitcoin')
# Adding path is mainly for running the script. 
# You can create an index.py and import the class instead
from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
import time
import json


ZERO_HASH = '0' * 64
VERSION = 1.0


class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        height = 0
        previous_hash = ZERO_HASH
        self.add_block(height, previous_hash)

    def add_block(self, height, previous_hash):
        timestamp = int(time.time())
        transaction = f"{height} Bitcoins has been mined successfully."
        merkle_root = hash256(transaction.encode()).hex()
        bits = 'ffff001f' # You can make this dynamic
        header = BlockHeader(VERSION, previous_hash,merkle_root, timestamp, bits)
        header.mine()
        self.chain.append(Block(height, 1, header.__dict__, 1, transaction).__dict__)
        print(json.dumps(self.chain, indent=4)) # This is to print output on console. You can remove it.

    def main(self):
        while True:
            last_block = self.chain[::-1]
            height = last_block[0]['height'] + 1
            previous_hash = last_block[0]['header']['hash']

            self.add_block(height, previous_hash)


if __name__ == '__main__':
    blockchain = Blockchain()
    blockchain.main()
