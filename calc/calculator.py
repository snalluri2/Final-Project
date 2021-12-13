from calc.history.calculations import Calculations

class Calculator:
    @staticmethod
    def get_last_result_value():
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    def addition(tuple_values: tuple):
        Calculations.add_addition_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def subtraction(tuple_values: tuple):
        Calculations.add_subtraction_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def multiplication(tuple_values: tuple):
        Calculations.add_multiplication_calculation_to_history(tuple_values)
        return True
    @staticmethod
    def getHistory():
        return Calculations.history
    @staticmethod
    def getHistoryFromCSV():
        return Calculations.readHistoryFromCSV()
    @staticmethod
    def writeHistoryToCSV():
        return Calculations.writeHistoryToCSV()