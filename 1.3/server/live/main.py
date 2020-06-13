

class HashTable:
    def __init__(self, init_length = 4):
        self.hash_table=dict()

    def hash(self, item):
        """
        Get the index of our array for a specific Transaction object.
        :param transaction:
        :return: int
        """
        return hash(item.transaction_id)

    def add(self, item):
        """Add a transaction to the hash-table

        :param transaction:Transaction
        :return:
        """
        index=self.hash(item)
        if index not in self.hash_table:
            self.hash_table[index]=item

    def get(self, item):
        """Get a transaction ID by the transaction object

        :param transaction: Transaction
        :return: bool
        """
        index=self.hash(item = item)

        if self.hash_table.get(index) != None:
            self.remove(index)
            print("Transaction Found !")
        else:
            print("Transaction Not Found !")

    def remove(self, index):
        """
        Removes the key-value on index place
        :param item: int
        :return:
        """
        del self.hash_table[index]

    def __str__(self):
        return f"{self.hash_table}"

class HashTableFactory:
    def __init__(self, data_frame):
        self.data_frame=data_frame

    def makeHashTable(self):

        hash_table=HashTable()

        for transaction in self.data_frame.transactions:
            hash_table.add(item = transaction)

        # print(hash_table.hash_table)
        # test_transaction = Transaction("15-03-2008", "72647", 4197.20)
        # print(hash_table.get(test_transaction))
        # print(hash_table.hash_table)
        # print(hash_table.get(test_transaction))

        # TODO
        return hash_table

# DataFrameFactory().makeDataFrame()


# print(transaction)
