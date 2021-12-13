"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    def get_result(self):
        result = 1.0
        for value in self.values:
            result = result * value
        return result
