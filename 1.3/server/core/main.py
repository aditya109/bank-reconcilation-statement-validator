from typing import List
import xlrd, datetime


class Transaction:
    """Transaction class creates a hashable object out of a transaction record
    """

    def __init__(self, date="", id=-1, amount=-1):
        self.__transaction_date = date
        self.__cheques_id = id
        self.__transaction_amount = amount

    @property
    def transaction_date(self):
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, date):
        self.__transaction_date = date

    @property
    def cheques_id(self):
        return self.__cheques_id

    @cheques_id.setter
    def cheques_id(self, id):
        self.__cheques_id = id

    @property
    def transaction_amount(self):
        return self.__transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, amount):
        self.__transaction_amount = amount

    def __str__(self):
        """Prints the requested details of transaction

        Returns:
            str: Returns a formatted string containing Transaction Details
        """
        return f"Transaction Details: \n" \
               f"Date   : {self.__transaction_date} \n" \
               f"ID     : {self.__cheques_id} \n" \
               f"Amount : {self.__transaction_amount} \n"

class DataFrame:
    """DataFrame create a compound object from a group of Transaction objects
        via Excel Files
    """

    def __init__(self):
        self.transactions = []
#
# class DataFrameFactory:
#     def makeDataFrame(self):
#         """TODO trying to manufacture dataframe"""
#         # index = 0
#         # length = len(transaction_dates)
#         # while index != length:
#         #     transaction = Transaction(transaction_dates[index], \
#         #                               transaction_id[index], \
#         #                               transaction_amount[index])
#         #     dataframe.transactions.append(transaction)
#         #     index += 1
#         # return dataframe
#
#         # # CDA Input
#         wb = xlrd.open_workbook("../assets/cda/cda.xls")
#         sheet = wb.sheet_by_index(0)
#         CDA_DataFrame = DataFrame()
#
#         rows = sheet.nrows
#         cols = sheet.ncols
#
#         for i in range(rows):
#             for j in range(cols):
#                 cell = sheet.cell_value(i, j)
#                 if j == 0:
#                     if cell == "":
#                         print(None, end="         ")
#                     else:
#                         print(xlrd.xldate.xldate_as_datetime(cell, wb.datemode).strftime("%d-%b-%Y"), end = "         ")
#                 elif j == 1:
#                     print(int(cell), end = "          ")
#                 else:
#                     print(cell, end = "\t")
#             print()
#
#         # CPNC Input
#         # wb = xlrd.open_workbook("../assets/cpnc/cpnc.xlsx")
#         # sheet = wb.sheet_by_index(0)
#
#         # rows = sheet.nrows
#         # cols = sheet.ncols
#
#         # for i in range(rows):
#         #     for j in range(cols):
#         #         cell = sheet.cell_value(i, j)
#         #         if cell == "TOTAL" : break
#         #         elif cell == "" or cell == "CASH":
#         #             print(cell, end="         ")
#         #         else:
#         #             if j == 0:
#         #                 print(xlrd.xldate.xldate_as_datetime(cell, wb.datemode).strftime("%d-%b-%Y"), end = "         ")
#         #             elif j == 1:
#         #                 print(int(cell), end = "          ")
#         #             else:
#         #                 print(cell, end = "\t")
#         #     print()
#
#         # # Credits Input
#         # wb = xlrd.open_workbook("../assets/cr/credit.xlsx")
#         # sheet = wb.sheet_by_index(0)
#
#         # rows = sheet.nrows
#         # cols = sheet.ncols
#
#         # for i in range(rows):
#         #     for j in range(cols):
#         #         cell = sheet.cell_value(i, j)
#         #         if cell == "" or cell == "CASH":
#         #             print(cell, end="\t")
#         #         else:
#         #             if j == 0:
#         #                 print(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y"), end="\t")
#         #             elif j == 1:
#         #                 print(cell, end = "         ")
#         #             else:
#         #                 print(cell, end = "         ")
#         #     print()
#
#         # # Debit Input
#         # wb = xlrd.open_workbook("../assets/dr/debit.xlsx")
#         # sheet = wb.sheet_by_index(0)
#
#         # rows = sheet.nrows
#         # cols = sheet.ncols
#
#         # for i in range(rows):
#         #     for j in range(cols):
#         #         cell = sheet.cell_value(i, j)
#         #         if cell == "" or cell == "CASH":
#         #             print(cell, end="\t")
#         #         else:
#         #             if j == 0:
#         #                 print(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y"), end="\t")
#         #             elif j == 1:
#         #                 print(cell[:10], end = "\t")
#         #             else:
#         #                 print(cell, end = "\t")
#         #     print()
#
# class HashTable:
#     def __init__(self, init_length = 4):
#         self.hash_table=dict()
#
#     def hash(self, item):
#         """
#         Get the index of our array for a specific Transaction object.
#         :param transaction:
#         :return: int
#         """
#         return hash(item.transaction_id)
#
#     def add(self, item):
#         """Add a transaction to the hash-table
#
#         :param transaction:Transaction
#         :return:
#         """
#         index=self.hash(item)
#         if index not in self.hash_table:
#             self.hash_table[index]=item
#
#     def get(self, item):
#         """Get a transaction ID by the transaction object
#
#         :param transaction: Transaction
#         :return: bool
#         """
#         index=self.hash(item = item)
#
#         if self.hash_table.get(index) != None:
#             self.remove(index)
#             print("Transaction Found !")
#         else:
#             print("Transaction Not Found !")
#
#     def remove(self, index):
#         """
#         Removes the key-value on index place
#         :param item: int
#         :return:
#         """
#         del self.hash_table[index]
#
#     def __str__(self):
#         return f"{self.hash_table}"
#
# class HashTableFactory:
#     def __init__(self, data_frame):
#         self.data_frame=data_frame
#
#     def makeHashTable(self):
#
#         hash_table=HashTable()
#
#         for transaction in self.data_frame.transactions:
#             hash_table.add(item = transaction)
#
#         # print(hash_table.hash_table)
#         # test_transaction = Transaction("15-03-2008", "72647", 4197.20)
#         # print(hash_table.get(test_transaction))
#         # print(hash_table.hash_table)
#         # print(hash_table.get(test_transaction))
#
#         # TODO
#         return hash_table

# DataFrameFactory().makeDataFrame()
# transaction = Transaction()
# transaction.transaction_date = "jklsadjkl"
# transaction.cheques_id = 1090909
# transaction.transaction_amount = 718927389172.90

# print(transaction)
