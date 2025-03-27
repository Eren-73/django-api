import json
from datetime import date , timedelta
from pprint import pprint

import requests


def get_rates(currencies,days=30):

    end_date = date.today()
    start_date=end_date-timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}"

    r = requests.get(requete)

    if not  r and r.json():
        return False, False

    api_rates = r.json().get("rates")

    all_rates = { currency:[] for currency in currencies }
    all_days = sorted(api_rates.keys())
    for each_day in all_days:
        [all_rates[currency].append(rate) for currency , rate in api_rates[each_day].items()]

    return all_days, all_rates


def stock(data, filename="F:\\PythonProject\\rates.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)  # Ajoute une indentation pour plus de lisibilité


if __name__ == '__main__':
    days,rates = get_rates(currencies=["USD","EUR","CAD","CHF"])
    pprint(days)
    pprint(rates)
    stock(rates)