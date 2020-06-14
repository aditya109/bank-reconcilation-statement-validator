import copy, time

from live.domain.module.hashtable import HashTable

start = time.time()
class TransactionFilter:
    def __init__(self, df1, df2):
        self.matcher = df1
        self.matching = df2

        self.result_matcher = copy.deepcopy(self.matcher)
        self.result_matching = copy.deepcopy(self.matching)

        self.hash_match_success = 0
        self.transaction_match_success = 0

    def find_hash(self, hash):
        print(f"Searching hash = {hash}", end=" ")
        if hash in self.matching.map:
            return True
        else:
            return False

    def find_transaction(self, transaction, hash):
        print(f"Searching amount = {transaction.transaction_amount}", end=" ")
        transactions_matching = self.matching.map[hash]
        for sample in transactions_matching:
            if sample.transaction_amount == transaction.transaction_amount:
                return True
        return False


    def trigger_filter(self):
        # print("Matching CPNC => Credits")
        # Iterating through each `hash, value` pair in self.matcher.map
        total_transactions = 0
        for hash, transactions in self.matcher.map.items():
            total_transactions += len(transactions)
            if self.find_hash(hash=hash):
                self.hash_match_success += 1
                print("Hash Match Found !")
                print("Matching solitary transactions", end=" ")
                for transaction in transactions:
                    if self.find_transaction(transaction=transaction, hash=hash):
                        self.transaction_match_success += 1
                        print("Amount Match Found !")
                    else:
                        print("Amount Not Match Found !")
            else:
                print("Hash Match Not Found !")
            print("==============================================================================")



        print(f"total hash in CPNC: {len(list(self.matcher.map.keys()))}")
        print(f"hash match found: {self.hash_match_success}")
        print(f"hash match not found: {len(list(self.matcher.map.keys())) - self.hash_match_success}")
        print(".......................................................................................")
        print(f"total transactions in CPNC: {total_transactions}")
        print(f"transaction match found: {self.transaction_match_success}")
        print(f"transaction match not found: {total_transactions-self.transaction_match_success}")
        print("........................................................................................")
        print("--- %s seconds FILTER---" % (time.time() - start))