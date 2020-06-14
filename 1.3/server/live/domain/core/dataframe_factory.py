import re
import time

import os, xlrd, datetime

from live.domain.core.transaction_builder import TransactionBuilder
from live.domain.core.dataframe import DataFrame


# start = time.time()
class DataFrameFactory:
    @staticmethod
    def build_date_step(workbook, cell, transaction:TransactionBuilder):
        """Adds transaction_date to TransactionBuilder

        @param workbook: excel workbook
        @type workbook: Book
        @param cell: cell data
        @type cell: str/int/float
        @param transaction: builder object
        @type transaction: TransactionBuilder
        @return: transaction builder object
        @rtype: TransactionBuilder
        """

        # checking for empty cell
        if cell == "":
            return transaction.onTransactionDate("NA")
        else:
            # converting normal date cell
            return transaction.onTransactionDate(str(datetime.datetime(*xlrd.xldate_as_tuple(cell, workbook.datemode)).strftime("%d-%b-%Y")))

    @staticmethod
    def build_id_step(cell, transaction:TransactionBuilder):
        """Adds cheques_id to TransactionBuilder

        @param cell: cell data
        @type cell: str/int/float
        @param transaction: builder object
        @type transaction: TransactionBuilder
        @return: transaction builder object
        @rtype: TransactionBuilder
        """
        # checking for empty cell
        if cell == "":
            return transaction.withChequeID("NA")
        else:
            # checking for str type cell
            if type(cell) == str:

                # checking if cell is `CASH`
                if cell == "CASH":
                    return transaction.withChequeID("CASH")

                # checking if cell has `CASH RECEIPT` in it, i.e., `AT BHAGALPUR -BHAGALPUR :- CASH RECEIPT`
                elif len(re.findall(r'(CASH RECEIPT)', str(cell))) == 1:
                    return transaction.withChequeID("CASH RECEIPT")

                # checking if cell contains account number,i.e.,`AT BHAGALPUR -LIC OF INDIA/ 072110200013581`
                elif len(re.findall(r'(\d{11,17})', str(cell))) != 0:
                    return transaction.withChequeID(re.findall(r'(\d{11,17})', str(cell))[0])
                # checking for just cheque numbers in cell
                elif len(re.findall(r'(\d{1,6})', str(cell))) != 0:
                    cell = re.findall(r'(\d{1,6})', str(cell))[0]
                    # making cheque numbers at least 6 digits
                    if len(str(cell)) != 6:
                        if len(str(cell)) != 6:
                            zeroes = 6 - len(str(cell))
                            temp = ""
                            for zero in range(zeroes):
                                temp = temp + "0"
                            cell = temp + str(cell)
                    return transaction.withChequeID(str(cell))
                else:
                    return transaction.withChequeID("NA")

            # checking for int/float type cell
            elif type(cell) == int or type(cell) == float:
                cell = str(int(cell))
                # making cheque numbers at least 6 digits
                if len(str(cell)) != 6:
                    if len(str(cell)) != 6:
                        zeroes = 6 - len(str(cell))
                        temp = ""
                        for zero in range(zeroes):
                            temp = temp + "0"
                        cell = temp + str(cell)
                return transaction.withChequeID(cell)

    @staticmethod
    def build_amount_step(cell, transaction:TransactionBuilder):
        """Adds transaction_amount to TransactionBuilder

         @param cell: cell data
        @type cell: str/int/float
        @param transaction: builder object
        @type transaction: TransactionBuilder
        @return: transaction builder object
        @rtype: TransactionBuilder
        """
        if cell == "":
            return transaction.withTransactionAmount(0)
        else:
            return transaction.withTransactionAmount(cell)



    @staticmethod
    def makeDataFrame(df_name, df_id, location):
        """Extracts rows as transactions for excel files, and manufactures DataFrame off
        transactions

        @type df_name:  str
        @type df_id:    str
        @type location: str

        @return: manufactured DataFrame
        @rtype: DataFrame
        """

        # opening excel workbook on location
        wb = xlrd.open_workbook(location)

        # accessing the first sheet from `wb`
        sheet = wb.sheet_by_index(0)

        # getting total rows and total columns from `sheet`
        rows, cols = sheet.nrows, sheet.ncols

        # initializing Dataframe object with `df_name` and `df_id`

        dataframe = DataFrame(name=df_name, id=df_id)

        # iterating for each row
        for i in range(rows):
            transaction = TransactionBuilder().start()
            for j in range(cols):
                cell = sheet.cell_value(i, j)
                if j == 0:
                    # adding transaction date to the builder
                    transaction = DataFrameFactory().build_date_step(workbook=wb, cell=cell, transaction=transaction)
                elif j == 1:
                    # adding cheques_id to the builder
                    transaction = DataFrameFactory().build_id_step(cell=cell, transaction=transaction)
                else:
                    # adding transaction_amount to the builder
                    transaction = DataFrameFactory().build_amount_step(cell=cell, transaction=transaction)
            # completed build of solitary transaction
            transaction = transaction.build()
            # adding dataframe
            dataframe.add_transaction(transaction=transaction)

        return dataframe


# print("--- %s seconds ---" % (time.time() - start))

# --- 0.2559232711791992 seconds ---
