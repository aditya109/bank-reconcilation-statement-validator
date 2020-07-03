import time

from live.lib.domain.module.hashtable import HashTable
import copy

class HashTableFactory:
    def __init__(self, data_frame):
        self.data_frame = copy.copy(data_frame)

    def makeHashTable(self):
        """Returns HashTable Object

        """
        hashtable = HashTable(id=self.data_frame.df_id)
        transactions = self.data_frame.get_transactions()

        for transaction in transactions:
            hashtable.add(item=transaction)

        self.data_frame.istat.benchmark_metadata.timestamp_of_hashtable_creation_completion = time.time()

        return hashtable
