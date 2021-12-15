from app.controllers.controller import ControllerBase

from tests.csvreader import Read

from flask import render_template

filename = "done/test.csv"

class TableController(ControllerBase):
    @staticmethod
    def get():
        df = Read.DataFrameFromCSVFile(filename)
        return render_template('rtable.html', titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)