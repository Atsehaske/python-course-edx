import requests
import sys

try:
    bitcoins = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
    sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    coindesk = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Requests's get error")
    sys.exit(1)

rate = coindesk.json()["bpi"]["USD"]["rate_float"]
amount = rate*bitcoins

print(f"${amount:,.4f}")
