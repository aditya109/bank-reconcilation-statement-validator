from live.domain.core.transaction import Transaction

class DataFrame:
    """DataFrame create a compound object from a group of Transaction objects
        via Excel Files
    """

    def __init__(self, name, id):
        self.df_name = name
        self.df_id = id
        self.df_len = 0
        self.__transactions = []

    def add_transaction(self, transaction:Transaction)-> bool:
        self.__transactions.append(transaction)
        self.df_len += 1

    def get_transactions(self):
        return self.__transactions

    def __str__(self):
        return f"DataFrame Details:\n" \
               f"DF_Name                  : {self.df_name}\n" \
               f"DF_ID                    : {self.df_id}\n" \
               f"DF_Dimensions            :{ self.df_len}\n"


