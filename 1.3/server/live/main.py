from live.domain.core.dataframe_factory import DataFrameFactory
from live.domain.module.hashtable_factory import HashTableFactory
from live.services.transaction_filter import TransactionFilter
import os, time

start = time.time()
def main():
    CPNC_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Cheque-Paid-Not-Credited", \
                                                                       df_id="CPNC", \
                                                                       location=os.getcwd().split(r"\live")[
                                                                                    0] + r"\assets\cpnc\cpnc.xlsx")).makeHashTable()

    CREDIT_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Credits", \
                                                                         df_id="CR", \
                                                                         location=os.getcwd().split("\\live")[
                                                                                      0] + "\\assets\\cr\\credit.xlsx")).makeHashTable()

    CDA_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Cheques-Dishonor-Action", \
                                                                      df_id="CDA", \
                                                                      location=os.getcwd().split("\\live")[
                                                                                   0] + "\\assets\\cda\\cda.xls")).makeHashTable()

    DEBIT_HashTable = HashTableFactory(DataFrameFactory().makeDataFrame(df_name="Debits", \
                                                                        df_id="DR", \
                                                                        location=os.getcwd().split("\\live")[
                                                                                     0] + "\\assets\\dr\\debit.xlsx")).makeHashTable()

    TransactionFilter(df1=CPNC_HashTable,
                      df2=CREDIT_HashTable).trigger_filter()
    print("--- %s seconds TOTAL---" % (time.time() - start))

if __name__ == '__main__':
    main()
