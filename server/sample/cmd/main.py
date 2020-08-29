import os
import time

start = time.time()


def filter_trigger():

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
    TransactionFilter(df1=CPNC_HashTable,
                      df2=CREDIT_HashTable).trigger_filter()
    # print("--- %s seconds TOTAL---" % (time.time() - start))
