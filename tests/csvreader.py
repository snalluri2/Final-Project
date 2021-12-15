import os

from tests.apath import abspath
import pandas as pd

filename = "../done/test.csv"

class Read:
    @staticmethod
    def DataFrameFromCSVFile(filename):
        return pd.read_csv(os.path.abspath(filename))