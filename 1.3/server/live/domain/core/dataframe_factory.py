import re
import time

import os, xlrd, datetime

from live.domain.core.transaction_builder import TransactionBuilder
from live.domain.core.dataframe import DataFrame


# start = time.time()
class DataFrameFactory:
    def makeDataFrame(self):
        """TODO trying to manufacture dataframe"""

        # CDA Input
        wb = xlrd.open_workbook(os.getcwd().split("\\live")[0]+"\\assets\\cda\\cda.xls")
        sheet = wb.sheet_by_index(0)
        CDA_DataFrame = DataFrame("Cheque-Dishonour-Action", "CDA")

        rows = sheet.nrows
        cols = sheet.ncols

        for i in range(rows):
            transaction = TransactionBuilder().start()
            for j in range(cols):
                cell = sheet.cell_value(i, j)
                if j == 0:
                    # transaction date
                    if cell == "":
                        transaction = transaction.onTransactionDate(None)
                    else:
                        transaction = transaction.onTransactionDate(str(xlrd.xldate.xldate_as_datetime(cell, wb.datemode).strftime("%d-%b-%Y")))
                elif j == 1:
                    # cheque id
                    if cell == "":
                        transaction = transaction.withChequeID(-1)
                    else:
                        transaction = transaction.withChequeID(int(cell))
                else:
                    if cell == "":
                        transaction = transaction.withTransactionAmount(-1)
                    else:
                        transaction = transaction.withTransactionAmount(float(cell))
            transaction = transaction.build()
            CDA_DataFrame.add_transaction(transaction=transaction)

        # CPNC Input
        wb = xlrd.open_workbook(os.getcwd().split("\\live")[0]+"\\assets\\cpnc\\cpnc.xlsx")
        sheet = wb.sheet_by_index(0)
        CPNC_DataFrame = DataFrame("Cheque-Paid-Not-Credited", "CPNC")

        rows = sheet.nrows
        cols = sheet.ncols

        for i in range(rows):
            transaction = TransactionBuilder().start()
            for j in range(cols):
                cell = sheet.cell_value(i, j)

                if cell == "TOTAL" : break
                else:
                    if j == 0:
                        # transaction date
                        if cell == "":
                            transaction = transaction.onTransactionDate(None)
                        else:
                            transaction = transaction.onTransactionDate(str(xlrd.xldate.xldate_as_datetime(cell, wb.datemode).strftime("%d-%b-%Y")))
                    elif j == 1:
                        # cheque id
                        if cell == ""or cell == "CASH":
                            transaction = transaction.withChequeID(cell)
                        else:
                            transaction = transaction.withChequeID((int(cell)))
                    else:
                        if cell == "":
                            transaction = transaction.withTransactionAmount(-1)
                        else:
                            transaction = transaction.withTransactionAmount(float(cell))
            transaction = transaction.build()
            CPNC_DataFrame.add_transaction(transaction=transaction)

        # Credits Input
        wb = xlrd.open_workbook(os.getcwd().split("\\live")[0]+"\\assets\\cr\\credit.xlsx")
        sheet = wb.sheet_by_index(0)
        CREDIT_DataFrame = DataFrame("Credits", "CR")

        rows = sheet.nrows
        cols = sheet.ncols

        for i in range(rows):
            transaction = TransactionBuilder().start()
            for j in range(cols):
                cell = sheet.cell_value(i, j)
                if j == 0:
                    # transaction date
                    if cell == "":
                        transaction = transaction.onTransactionDate(None)
                    else:
                        transaction = transaction.onTransactionDate(str(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y")))
                elif j == 1:
                    # cheque id
                    if len(re.findall(r'(\d{11,17})', cell)) != 0:
                        transaction = transaction.withChequeID(re.findall(r'(\d{11,17})', cell)[0])
                    elif len(re.findall(r'(\d{6})', cell)) != 0:
                        transaction = transaction.withChequeID(re.findall(r'(\d{1,6})', cell)[0])
                    elif len(re.findall(r'(CASH RECEIPT)', cell)) == 1:
                        transaction = transaction.withChequeID("CASH RECEIPT")
                    else:
                        transaction = transaction.withChequeID("NA")
                else:
                    # transaction amount
                    if cell == "":
                        transaction = transaction.withTransactionAmount(-1)
                    else:
                        transaction = transaction.withTransactionAmount(float(cell))
            transaction = transaction.build()
            CREDIT_DataFrame.add_transaction(transaction=transaction)

        # Debit Input
        wb = xlrd.open_workbook(os.getcwd().split("\\live")[0]+"\\assets\\dr\\debit.xlsx")
        sheet = wb.sheet_by_index(0)
        DEBIT_DataFrame = DataFrame("Debits", "DR")

        rows = sheet.nrows
        cols = sheet.ncols

        for i in range(rows):
            transaction = TransactionBuilder().start()
            for j in range(cols):
                cell = sheet.cell_value(i, j)
                if j == 0:
                    if cell == "":
                        transaction = transaction.onTransactionDate(None)
                    else:
                        transaction = transaction.onTransactionDate(str(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y")))
                elif j == 1:
                    # cheque id
                    if len(re.findall(r'(\d{11,17})', cell)) != 0:
                        transaction = transaction.withChequeID(re.findall(r'(\d{11,17})', cell)[0])
                    elif len(re.findall(r'(\d{6})', cell)) != 0:
                        transaction = transaction.withChequeID(re.findall(r'(\d{1,6})', cell)[0])
                    elif len(re.findall(r'(CASH RECEIPT)', cell)) == 1:
                        transaction = transaction.withChequeID("CASH RECEIPT")
                    else:
                        transaction = transaction.withChequeID("NA")
                else:
                    transaction = transaction.withTransactionAmount(float(cell))
            transaction = transaction.build()
            DEBIT_DataFrame.add_transaction(transaction=transaction)
        # print(DEBIT_DataFrame,"\n" , CREDIT_DataFrame, "\n" ,CDA_DataFrame, "\n" ,CPNC_DataFrame)

        return CDA_DataFrame, CPNC_DataFrame, CREDIT_DataFrame, DEBIT_DataFrame


# DataFrameFactory().makeDataFrame()
# print("--- %s seconds ---" % (time.time() - start))

# --- 0.2559232711791992 seconds ---
