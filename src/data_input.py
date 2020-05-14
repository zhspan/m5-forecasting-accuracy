"""
Read data and keep it cached
"""

import pandas as pd

class DataLoader:

    def __init__(self, input_directory="../input/m5-forecasting-accuracy"):
        """
        :param input_directory: Location of input files
        :type input_directory: string
        """
        self.input_directory = input_directory
        self.sample_submission = None
        self.sales_train_validation = None
        self.calendar = None
        self.sell_prices = None

    def get_sample_submission(self):
        """
        :return: a copy of the sample submission DataFrame
        :rtype: pandas.DataFrame
        """
        if self.sample_submission is None:
            self.sample_submission = pd.read_csv(
                    self.input_directory + "/sample_submission.csv")
        return self.sample_submission.copy()
    
    def get_sales_train_validation(self):
        """
        :return: a copy of the sales_train_validation DataFrame
        :rtype: pandas.DataFrame
        """
        if self.sales_train_validation is None:
            self.sales_train_validation = pd.read_csv(
                    self.input_directory + "/sales_train_validation.csv")
        return self.sales_train_validation.copy()

    def get_calendar(self):
        """
        :return: a copy of the calendar DataFrame
        :rtype: pandas.DataFrame
        """
        if self.calendar is None:
            self.calendar = pd.read_csv(
                    self.input_directory + "/calendar.csv")
        return self.calendar.copy()

    def get_sell_prices(self):
        """
        :return: a copy of the sell prices DataFrame
        :rtype: pandas.DataFrame
        """
        if self.sell_prices is None:
            self.sell_prices = pd.read_csv(
                    self.input_directory + "/sell_prices.csv")
        return self.sell_prices.copy()

