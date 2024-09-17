import requests
import sys

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        jsoned = response.json()
        rate_float = jsoned['bpi']['USD']['rate_float']

    except requests.RequestException:
        print("Some problems with API")

    if len(sys.argv) == 2:
        try:
            argument = float(sys.argv[1])

            if argument.is_integer():
                argument = int(argument)
                total = argument * rate_float
                print(f"${total:,.4f}")
            elif isinstance(argument,float):
                argument = float(argument)
                total = argument * rate_float
                print(f"${total:,.4f}")


        except ValueError:
            sys.exit(1)
    else:
        sys.exit(1)




main()
