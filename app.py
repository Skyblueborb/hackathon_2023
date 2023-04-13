from math import exp
from typing import Dict
from flask import Flask, redirect, render_template, request
from currency import *

app = Flask(__name__)


NOMINALS = Counter()
CALC = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/converter", methods=["GET", "POST"])
def converter():
    global NOMINALS
    global CALC

    if request.method == "GET":
        nominals, calc = NOMINALS, CALC
        NOMINALS, CALC = Counter(), 0
        return render_template("converter.html", nominals=nominals, calc=calc)

    if request.method == "POST":
        sum = request.form.get("sum")
        if "-" in sum:
            return redirect("/converter")
        year = request.form.get("year")
        try:
            fact = factor(int(year))
        except (NotImplementedError, ValueError):
            return redirect("/converter")
        CALC = calculate(float(sum), fact)
        NOMINALS = getNominals(CALC)

        return redirect("/converter")
