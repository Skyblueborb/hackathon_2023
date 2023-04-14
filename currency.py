import requests
from bs4 import BeautifulSoup
from collections import Counter
from math import floor
from re import sub

DOLLAR_COURSE_FACTOR = 100.0
CURRENT_PAY = 76153.80
ZUS = "https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/wskazniki/przecietne-wynagrodzenie-w-latach"
MONEY_DICT = {0: "static/csv/nominals.csv", 1: "static/csv/dollars.csv"}

polishify = lambda num: str(round(num, 2)).replace(".", ",")

def csv_reader(path: str) -> dict[float, str]:
    if not isinstance(path, str):
        raise TypeError
    with open(path, "r") as file:
        rawData = []
        for i in file:
            rawData.append(i[:-1])
        data = [i.split(",") for i in rawData]
        return {numCleaner(i[0]): i[1] for i in data}


def numCleaner(number: str) -> float:  # czyści wprowadzoną wartość z dziwnych formatacji
    output = number.replace(" ", "", -1).replace(",", ".", -1)
    try:
        return float(output)
    except Exception:
        raise ValueError


def factor(year: int) -> float:  # średnia pensja dla roku [year]
    if year not in range(1960, 1980):
        raise NotImplementedError  # robimy tylko dla lat 1960-79
    soup = BeautifulSoup(requests.get(ZUS).text, "html.parser")
    return numCleaner(
        (soup.select(".zus-cms>table>tbody>tr>td")[1::3][year - 1950]).text
    )


calculate = lambda amount, fact: (
-1 if amount < 0 else round((amount / CURRENT_PAY) * fact, 2)
)  # (-1): error


def getNominals(money: float, currencyType = 0) -> Counter[str]:
    print(currencyType)
    if currencyType != 0 and currencyType != 1:
        raise ValueError
    if currencyType == 1:
        money = round(money / DOLLAR_COURSE_FACTOR, 2)
    noms = csv_reader(MONEY_DICT[currencyType])
    count = Counter()
    curMoney = money + 0.00001
    for val, nom in reversed(noms.items()):
        temp = floor(curMoney // val)
        if temp:
            count[nom] += temp
            curMoney -= val * temp
    return count
print(polishify(1234.56))