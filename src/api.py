from datetime import date, timedelta
from pprint import pprint

import requests

adress_requet_01 = "https://api.exchangerate.host/latest"
adress_requet_02 = "https://api.exchangerate.host/timeseries?start_date=2020-01-01&end_date=2020-01-04"
adress_requet_03 = "https://api.exchangerate.host/timeseries?start_date=2020-10-01&end_date=2020-10-03&symbols=USD,CAD"
doc_api = "https://exchangerate.host/#/#docs"


def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"
    response = requests.get(requete)

    if not response and not response.json():
        return False, False

    api_rates = response.json().get("rates")
    all_days = sorted(api_rates.keys())
    all_rates = {currency: [] for currency in currencies}

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates


if __name__ == '__main__':
    days, rates = get_rates(["AUD", "UAH"])


