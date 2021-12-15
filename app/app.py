"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.table_controller import TableController
from app.controllers.gloss_controller import GlossController



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/rtable", methods=['GET'])
def table_get():
    return TableController.get()

@app.route("/gloss", methods=['GET'])
def gloss_get():
    return GlossController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()