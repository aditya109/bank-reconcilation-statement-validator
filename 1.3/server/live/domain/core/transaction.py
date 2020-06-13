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
        return f"Transaction Details: " \
               f"Date   : {self.__transaction_date} " \
               f"ID     : {self.__cheques_id} " \
               f"Amount : {self.__transaction_amount} "
