from app.controllers.controller import ControllerBase

from flask import render_template

class GlossController(ControllerBase):
    @staticmethod
    def get():
        return render_template('gloss.html')
