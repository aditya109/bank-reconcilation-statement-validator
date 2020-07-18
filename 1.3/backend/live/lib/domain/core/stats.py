from typing import Any


class LStat:
    def __init__(self):
        self.i_stats = []


class IStat:
    def __init__(self):
        self.name_metadata = NameMetadata()
        self.benchmark_metadata = BenchmarkMetadata()
        self.record_metadata = RecordMetadata()

    def __str__(self):
        formatted_stats = str()
        formatted_stats = f"{formatted_stats}Individual Stats:\n" \
                          f"======================================\n" \
                          f"-----------NAME METADATA--------------\n" \
                          f"DataFrame Full Name : {self.name_metadata.df_name_full}\n" \
                          f"DataFrame Alias     : {self.name_metadata.df_name_short}\n" \
                          f"=======================================\n" \
                          f"---------BENCHMARK METADATA------------\n" \
                          f"Duration >>>>" \
                          f"File Split : "

class NameMetadata:

    def __init__(self, df_name_short="", df_name_full=""):
        self.__df_name_short = df_name_short #OK
        self.__df_name_full = df_name_full #OK

        @property
        def df_name_short(self):
            return self.__df_name_short

        @df_name_short.setter
        def df_name_short(self, df_name_short):
            self.__df_name_short = df_name_short

        @property
        def df_name_full(self):
            return self.__df_name_full

        @df_name_full.setter
        def df_name_full(self, df_name_full):
            self.__df_name_full = df_name_full


class BenchmarkMetadata:
    def __init__(self, timestamp_of_file_split = None, timestamp_of_df_creation_completion = None, timestamp_of_hashtable_creation_completion = None, timestamp_of_file_filtering = None, timestamp_of_file_finalization = None,
                 duration_of_file_compilation = None):
        self.__timestamp_of_hashtable_creation_completion = timestamp_of_hashtable_creation_completion #OK
        self.__timestamp_of_df_creation_completion = timestamp_of_df_creation_completion #OK
        self.__timestamp_of_file_split = timestamp_of_file_split #OK
        self.__timestamp_of_file_filtering = timestamp_of_file_filtering
        self.__timestamp_of_file_finalization = timestamp_of_file_finalization
        self.__duration_of_file_compilation = duration_of_file_compilation

    @property
    def timestamp_of_df_creation_completion(self):
        return self.__timestamp_of_df_creation_completion

    @timestamp_of_df_creation_completion.setter
    def timestamp_of_df_creation_completion(self, timestamp_of_df_creation_completion):
        self.__timestamp_of_df_creation_completion = timestamp_of_df_creation_completion

    @property
    def timestamp_of_hashtable_creation_completion(self):
        return self.__timestamp_of_hashtable_creation_completion

    @timestamp_of_hashtable_creation_completion.setter
    def timestamp_of_hashtable_creation_completion(self, timestamp_of_hashtable_creation_completion):
        self.__timestamp_of_hashtable_creation_completion = timestamp_of_hashtable_creation_completion

    @property
    def timestamp_of_file_split(self):
        return self.__timestamp_of_file_split

    @timestamp_of_file_split.setter
    def timestamp_of_file_split(self, timestamp_of_file_split):
        self.__timestamp_of_file_split = timestamp_of_file_split

    @property
    def timestamp_of_file_filtering(self):
        return self.__timestamp_of_file_filtering

    @timestamp_of_file_filtering.setter
    def timestamp_of_file_filtering(self, timestamp_of_file_filtering):
        self.__timestamp_of_file_filtering = timestamp_of_file_filtering

    @property
    def timestamp_of_file_finalization(self):
        return self.__timestamp_of_file_finalization

    @timestamp_of_file_finalization.setter
    def timestamp_of_file_finalization(self, timestamp_of_file_finalization):
        self.__timestamp_of_file_finalization = timestamp_of_file_finalization

    @property
    def duration_of_file_compilation(self):
        return self.__duration_of_file_compilation

    @duration_of_file_compilation.setter
    def duration_of_file_compilation(self, duration_of_file_compilation):
        self.__duration_of_file_compilation = duration_of_file_compilation


class RecordMetadata:
    def __init__(self, total_transactions_initial = 0, total_cash_initial = 0.0, total_transactions_final = 0, total_cash_final = 0.0,
                 transactions_redundant = 0, transactions_non_redundant = 0, cash_found = 0.0, cash_not_found = 0):
        self.__transactions_non_redundant = transactions_non_redundant
        self.__transactions_redundant = transactions_redundant
        self.__total_cash_final = total_cash_final
        self.__total_transactions_final = total_transactions_final
        self.__total_cash_initial = total_cash_initial #OK
        self.__total_transactions_initial = total_transactions_initial #OK
        self.__cash_found = cash_found
        self.__cash_not_found = cash_not_found

    @property
    def transactions_non_redundant(self):
        return self.__transactions_non_redundant

    @transactions_non_redundant.setter
    def transactions_non_redundant(self, transactions_non_redundant):
        self.__transactions_non_redundant = transactions_non_redundant

    @property
    def transactions_redundant(self):
        return self.__transactions_redundant

    @transactions_redundant.setter
    def transactions_redundant(self, transactions_redundant):
        self.__transactions_redundant = transactions_redundant

    @property
    def total_cash_final(self):
        return self.__total_cash_final

    @total_cash_final.setter
    def total_cash_final(self, total_cash_final):
        self.__total_cash_final = total_cash_final

    @property
    def total_transactions_final(self):
        return self.__total_transactions_final

    @total_transactions_final.setter
    def total_transactions_final(self, total_transactions_final):
        self.__total_transactions_final = total_transactions_final

    @property
    def total_cash_initial(self):
        return self.__total_cash_initial

    @total_cash_initial.setter
    def total_cash_initial(self, total_cash_initial):
        self.__total_cash_initial = total_cash_initial

    @property
    def total_transactions_initial(self):
        return self.__total_transactions_initial

    @total_transactions_initial.setter
    def total_transactions_initial(self, total_transactions_initial):
        self.__total_transactions_initial = total_transactions_initial

    @property
    def cash_found(self):
        return self.__cash_found

    @cash_found.setter
    def cash_found(self, cash_found):
        self.__cash_found = cash_found

    @property
    def cash_not_found(self):
        return self.__cash_not_found

    @cash_not_found.setter
    def cash_not_found(self, cash_not_found):
        self.__cash_not_found = cash_not_found



