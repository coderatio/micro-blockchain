class Block:
    """
    Block is a storage container
    """

    def __init__(self, height, size, header, tx_count, transactions):
        self.height = height
        self.size = size
        self.header = header
        self.tx_count = tx_count
        self.txs = transactions

