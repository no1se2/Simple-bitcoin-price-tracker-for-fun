import requests
import time
import platform
from datetime import datetime
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def getprice():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur,gbp,ils"
    previous_prices = {}
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            price = data["bitcoin"]["usd"]
            price2 = data["bitcoin"]["eur"]
            price3 = data["bitcoin"]["gbp"]
            price4 = data["bitcoin"]["ils"]
            timenow = datetime.now()
            formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")
            
            def get_arrow(curr, prev):
                if prev is None:
                    return "-"
                return f"{Fore.GREEN}↑ Up" if curr > prev else f"{Fore.RED}↓ Down" if curr < prev else f"{Fore.WHITE}- No change in price"

            usd_arrow = get_arrow(price, previous_prices.get("usd"))
            clear()
            print(f"{Fore.GREEN}Last updated: {formatted_time}")
            print(f"{Fore.GREEN}----------------------------------------")
            print(f"USD: ${price} {usd_arrow}")
            print(f"ILS: ₪{price4}")
            print(f"EUR: €{price2}")
            print(f"GBP: £{price3}")
            print(f"{Fore.GREEN}----------------------------------------")

            previous_prices["usd"] = price

            time.sleep(30)
        except KeyError:
            print("there was an error getting the price.")
        except requests.exceptions.RequestException as e:
            print(f"There was a problem with the network: {e}")

clear()
getprice()
