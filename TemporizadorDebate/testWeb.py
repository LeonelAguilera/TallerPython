# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:25:21 2023

@author: MrWenas
"""

#streamlit
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()