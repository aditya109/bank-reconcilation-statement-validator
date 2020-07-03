import os
import time

from live.lib.domain.core.dataframe_factory import DataFrameFactory
from live.lib.domain.module.hashtable_factory import HashTableFactory

start = time.time()


def filter_trigger():
    PROJECT_DIRECTORY = os.getcwd().split(r"bank-reconcilation-statement-validator\1.3\server")[0]
    SERVER_ABSOLUTE_PATH = PROJECT_DIRECTORY + r"bank-reconcilation-statement-validator\1.3\server"
    INPUT_FILE_SOURCE_DIRECTORY = SERVER_ABSOLUTE_PATH + r"\live\static"
    # logic for finding the most recent file
    path = os.getcwd()
    os.chdir(INPUT_FILE_SOURCE_DIRECTORY)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    #
    file = INPUT_FILE_SOURCE_DIRECTORY + f"\\{newest}"
    os.chdir(path)



    CPNC_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Cheque-Paid-Not-Credited",
                                                                       df_id="CPNC",
                                                                       location=file)).makeHashTable()

    CREDIT_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Credits",
                                                                         df_id="Cr",
                                                                         location=file)).makeHashTable()

    CDA_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Cheques-Dishonor-Action",
                                                                      df_id="CDA",
                                                                      location=file)).makeHashTable()

    DEBIT_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Debits",
                                                                        df_id="dr",
                                                                        location=file)).makeHashTable()
    #
    # TransactionFilter(df1=CPNC_HashTable,
    #                   df2=CREDIT_HashTable).trigger_filter()
    # print("--- %s seconds TOTAL---" % (time.time() - start))
    pass


filter_trigger()
