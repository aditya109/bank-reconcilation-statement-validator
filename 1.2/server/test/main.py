class Transaction:
    def __init__(self, date: str, id: str, amount: int):
        self.transaction_date = date
        self.transaction_id = id
        self.transaction_amount = amount

    def __str__(self):
        return f"Transaction Details: \n" \
               f"Date   : {self.transaction_date} \n" \
               f"ID     : {self.transaction_id} \n" \
               f"Amount : {self.transaction_amount} \n"

class DataFrame:
    def __init__(self):
        self.transactions = []
        self.locations = []

    def add_locations(self, location):
        self.locations.append(location)

class DataFrameFactory:
    def makeDataFrame(self):
        """TODO trying to manufacture dataframe"""

        file = open("./transactiondates.txt", "r")
        transaction_dates = file.read().split("\n")
        file.close()

        file = open("./chq.txt", "r")
        transaction_id = file.read().split("\n")
        file.close()

        file = open("./amount.txt", "r")
        transaction_amount = file.read().split("\n")
        file.close()

        index = 0
        length = len(transaction_dates)
        dataframe = DataFrame()
        while index != length:
            transaction = Transaction(transaction_dates[index], \
                                      transaction_id[index], \
                                      transaction_amount[index])
            dataframe.transactions.append(transaction)
            index += 1
        return dataframe

class HashTable:
    def __init__(self, init_length=4):
        self.hash_table = dict()

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
        index = self.hash(item)
        if index not in self.hash_table:
            self.hash_table[index] = item

    def get(self, item):
        """Get a transaction ID by the transaction object

        :param transaction: Transaction
        :return: bool
        """
        index = self.hash(item=item)

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
        self.data_frame = data_frame

    def makeHashTable(self):

        hash_table = HashTable()

        for transaction in self.data_frame.transactions:
            hash_table.add(item=transaction)

        # print(hash_table.hash_table)
        # test_transaction = Transaction("15-03-2008", "72647", 4197.20)
        # print(hash_table.get(test_transaction))
        # print(hash_table.hash_table)
        # print(hash_table.get(test_transaction))

        #TODO
        return hash_table





cpnc_dataframe = DataFrameFactory().makeDataFrame()

HashTableFactory(data_frame=cpnc_dataframe).makeHashTable()

test_transaction = Transaction("15-03-2008", "72647", 4197.20)