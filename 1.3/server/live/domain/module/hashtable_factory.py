from live.domain.module.hashtable import HashTable


class HashTableFactory:
    def __init__(self, data_frame):
        self.data_frame=data_frame


    def makeHashTable(self):
        """Returns HashTable Object

        """
        hashtable=HashTable(id = self.data_frame.df_id)
        transactions = self.data_frame.get_transactions()

        for transaction in transactions:
            hashtable.add(item = transaction)

        return hashtable


