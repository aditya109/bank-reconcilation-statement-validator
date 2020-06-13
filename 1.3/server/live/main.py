import re

from live.domain.core.dataframe_factory import DataFrameFactory
from live.domain.module.hashtable_factory import HashTableFactory

def main() :
    CDA_DataFrame, CPNC_DataFrame, CREDIT_DataFrame, DEBIT_DataFrame = DataFrameFactory().makeDataFrame()

    for t in CPNC_DataFrame.get_transactions():
        print(t)
    print(CPNC_DataFrame)
    for t in CREDIT_DataFrame.get_transactions():
        print(t)
    print(CREDIT_DataFrame)

    # print(DEBIT_DataFrame, "\n", CREDIT_DataFrame, "\n", CDA_DataFrame, "\n", CPNC_DataFrame)
    # CDA_HashTable = HashTableFactory(data_frame=CDA_DataFrame).makeHashTable()
    # CPNC_HashTable = HashTableFactory(data_frame=CPNC_DataFrame).makeHashTable()
    # CREDIT_HashTable = HashTableFactory(data_frame=CREDIT_DataFrame).makeHashTable()
    # DEBIT_HashTable = HashTableFactory(data_frame=DEBIT_DataFrame).makeHashTable()



if __name__ == '__main__':
    main()