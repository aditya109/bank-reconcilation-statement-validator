import xlrd, datetime

from live.domain.core.transaction_builder import TransactionBuilder
from live.domain.core.dataframe import DataFrame



class DataFrameFactory:
    def makeDataFrame(self):
        """TODO trying to manufacture dataframe"""

        # CDA Input
        wb = xlrd.open_workbook("../../../assets/cda/cda.xls")
        sheet = wb.sheet_by_index(0)
        CDA_DataFrame = DataFrame("Cheque-Dishonour-Action", "CDA")

        rows = sheet.nrows
        cols = sheet.ncols

        # transaction = TransactionBuilder().start().onTransactionDate("12-Dec-2019")
        # transaction = transaction.withChequeID("109090")
        # transaction = transaction.withTransactionAmount("21312321312321.97")
        # transaction = transaction.build()
        # print(transaction)

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
        print(CDA_DataFrame)
            # break
        # CPNC Input
        # wb = xlrd.open_workbook("../assets/cpnc/cpnc.xlsx")
        # sheet = wb.sheet_by_index(0)
        #
        # rows = sheet.nrows
        # cols = sheet.ncols
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         cell = sheet.cell_value(i, j)
        #         if cell == "TOTAL" : break
        #         elif cell == "" or cell == "CASH":
        #             print(cell, end="         ")
        #         else:
        #             if j == 0:
        #                 print(xlrd.xldate.xldate_as_datetime(cell, wb.datemode).strftime("%d-%b-%Y"), end = "         ")
        #             elif j == 1:
        #                 print(int(cell), end = "          ")
        #             else:
        #                 print(cell, end = "\t")
        #     print()

        # Credits Input
        # wb = xlrd.open_workbook("../assets/cr/credit.xlsx")
        # sheet = wb.sheet_by_index(0)
        #
        # rows = sheet.nrows
        # cols = sheet.ncols
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         cell = sheet.cell_value(i, j)
        #         if cell == "" or cell == "CASH":
        #             print(cell, end="\t")
        #         else:
        #             if j == 0:
        #                 print(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y"), end="\t")
        #             elif j == 1:
        #                 print(cell, end = "         ")
        #             else:
        #                 print(cell, end = "         ")
        #     print()

        # Debit Input
        # wb = xlrd.open_workbook("../assets/dr/debit.xlsx")
        # sheet = wb.sheet_by_index(0)
        #
        # rows = sheet.nrows
        # cols = sheet.ncols
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         cell = sheet.cell_value(i, j)
        #         if cell == "" or cell == "CASH":
        #             print(cell, end="\t")
        #         else:
        #             if j == 0:
        #                 print(datetime.datetime(*xlrd.xldate_as_tuple(cell, wb.datemode)).strftime("%d-%b-%Y"), end="\t")
        #             elif j == 1:
        #                 print(cell[:10], end = "\t")
        #             else:
        #                 print(cell, end = "\t")
        #     print()

DataFrameFactory().makeDataFrame()