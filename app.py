from math import exp
from typing import Dict
from flask import Flask, redirect, render_template, request
from currency import *

app = Flask(__name__)


NOMINALS = Counter()
CALC = 0
YEAR = 1970


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/converter", methods=["GET", "POST"])
def converter():
    global NOMINALS
    global CALC
    global YEAR

    if request.method == "GET":
        nominals, calc, year = NOMINALS, CALC, YEAR
        NOMINALS, CALC, YEAR = Counter(), 0, 1970
        return render_template(
            "converter.html", nominals=nominals, calc=calc, year=year
        )

    if request.method == "POST":
        sum = request.form.get("sum")
        if "-" in sum:
            return redirect("/converter")
        YEAR = request.form.get("year")
        try:
            fact = factor(int(YEAR))
            CALC = calculate(numCleaner(sum), fact)
        except (NotImplementedError, ValueError):
            return redirect("/converter")
        NOMINALS = getNominals(CALC)

        return redirect("/converter")
