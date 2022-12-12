import requests
import json

base_currency = input().lower()
base_currency_json = requests.get(f"http://www.floatrates.com/daily/{base_currency}.json")
base_currency_all = json.loads(base_currency_json.text)
bank_cache = {}
if "usd" in base_currency_all:
    bank_cache["usd"] = base_currency_all["usd"]["rate"]
if "eur" in base_currency_all:
    bank_cache["eur"] = base_currency_all["eur"]["rate"]

while currency_query := input().lower():
    money_query = float(input())
    print("Checking the cache...")
    if bank_cache.get(currency_query):
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        bank_cache[currency_query] = base_currency_all[currency_query]["rate"]
    print(f"You received {round((bank_cache[currency_query] * money_query), 2)} {currency_query.upper()}")
