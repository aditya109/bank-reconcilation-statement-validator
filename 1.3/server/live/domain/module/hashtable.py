

class HashTable:
    def __init__(self, id = ""):
        self.map=dict()
        self.map_id = id

    def hash(self, item):
        """
        Get the index of our array for a specific Transaction object.
        :param transaction:
        :return: int
        """
        return hash(item.cheques_id)

    def add(self, item):
        """Add a transaction to the hash-table

        :param transaction:Transaction
        :return:
        """
        index=self.hash(item)
        if index not in self.map:
            self.map[index]=item

    def get(self, item):
        """Get a transaction ID by the transaction object

        :param transaction: Transaction
        :return: bool
        """
        index=self.hash(item = item)

        if self.map.get(index) != None:
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
        del self.map[index]

    def __str__(self):
        return f"{self.map}"
