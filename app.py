from math import exp
from typing import Dict
from flask import Flask, redirect, render_template, request
from currency import *

app = Flask(__name__)


NOMINALS = Counter()
CALC = 0
YEAR = 1970
INFO = ""
CURRENCY = 1

@app.route("/")
def index():
    return render_template("index.html", show_button=0)


@app.route("/converter", methods=["GET", "POST"])
def converter():
    global NOMINALS
    global CALC
    global YEAR
    global INFO
    global CURRENCY

    if request.method == "GET":
        nominals, calc, year, info, currency = NOMINALS, CALC, YEAR, INFO, CURRENCY
        NOMINALS, CALC, YEAR, INFO, CURRENCY = Counter(), 0, 1970, "", 0
        return render_template(
            "converter.html", nominals=nominals, calc=calc, year=year, info=info, show_button=1, currency=currency
        )
    if request.method == "POST":
        sum = request.form.get("sum")
        if "-" in sum:
            return redirect("/converter")
        YEAR = request.form.get("year")
        CURRENCY = int(request.form.get("currency"))
        print(CURRENCY)
        try:
            fact = factor(int(YEAR))
            CALC = calculate(numCleaner(sum), fact)
        except (NotImplementedError, ValueError):
            return redirect("/converter")
        NOMINALS = getNominals(CALC, CURRENCY)
        INFO = f"W roku {YEAR} to: {polishify(CALC/(DOLLAR_COURSE_FACTOR if CURRENCY == 1 else 1))} {'$' if CURRENCY == 1 else 'zł'}"
        return redirect("/converter")

@app.route("/moda")
def moda():
    return render_template("moda.html", show_button=0)

@app.route("/mapa")
def mapa():
    return render_template("mapa.html", show_button=1)

