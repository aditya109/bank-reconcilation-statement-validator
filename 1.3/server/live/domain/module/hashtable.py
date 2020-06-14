import hashlib
class HashTable:
    def __init__(self, id = ""):
        self.map =dict()
        self.map_id = id

    @staticmethod
    def hash_item(item):
        """
        Get the index of our array for a specific Transaction object.
        :param transaction:
        :return: int
        """
        h = hashlib.md5()
        h.update(str(item).encode('utf-8'))
        return h.hexdigest()

    def add(self, item):
        """Add a transaction to the hash-table

        :param transaction:Transaction
        :return:
        """
        index = HashTable.hash_item(item.cheques_id)
        if index not in self.map:
            self.map[index ] =[item]
        else:
            self.map[index].append(item)

    def get(self, item):
        """Get a transaction ID by the transaction object

        :param transaction: Transaction
        :return: bool
        """
        index=HashTable.hash_item(item = item.cheques_id)

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
        return f"HashTable :\n" \
               f"HT_ID: {self.map_id}" \
               # f"HT_Size: {self.map}"
