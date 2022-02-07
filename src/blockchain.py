from src.core.block import Block
from src.core.blockheader import BlockHeader
from src.util.util import hash256, random_bits
import time
import json
import sys


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
        bits = random_bits()  # You can make this dynamic
        header = BlockHeader(VERSION, previous_hash, merkle_root, timestamp, bits)
        header.mine()
        trx_count = len(self.chain) + 1
        block_size = self.__get_block_size(height, header, trx_count, transaction)
        
        self.chain.append(Block(height, hex(block_size), header.__dict__, trx_count, transaction).__dict__)
        print(json.dumps(self.chain, indent=4))  # This is to print output on console. You can remove it.

    @staticmethod
    def __get_block_size(height, header, trx_count, transaction):
        block_data = [
            {
                height: height,
                header: header.__dict__,
                trx_count: trx_count,
                transaction: transaction
            }
        ]

        return sys.getsizeof(block_data)

    def run(self):
        while True:
            last_block = self.chain[::-1]
            last_block_height = last_block[0]['height']
            new_height = last_block_height
            height = hex(new_height + 1) if isinstance(last_block_height, int)  else hex(int(new_height, base=16) + 1)
            previous_hash = last_block[0]['header']['hash']

            self.add_block(height, previous_hash)
