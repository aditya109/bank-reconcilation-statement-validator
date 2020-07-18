from live.lib.domain.core.transaction import Transaction

class TransactionBuilder:
    def __init__(self):
        self.date = ""
        self.id = ""
        self.amount = ""

    @staticmethod
    def start():
        return TransactionBuilder()

    def onTransactionDate(self, date):
        self.date = date
        return self

    def withChequeID(self, id):
        self.id = id
        return self

    def withTransactionAmount(self, amount):
        self.amount = amount
        return self

    def build(self):
        return Transaction(self.date, self.id, self.amount)



# transaction = TransactionBuilder().start().onTransactionDate("12-Dec-2019")
# transaction = transaction.withChequeID("109090")
# transaction = transaction.withTransactionAmount("21312321312321.97")
# transaction = transaction.build()
# print(transaction)