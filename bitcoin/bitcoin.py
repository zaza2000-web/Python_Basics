import requests
import sys

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        jsoned = response.json()
        rate_float = jsoned['bpi']['USD']['rate']

    except requests.RequestException:
        print("Some problems with API")

    if len(sys.argv) == 2:
        try:
            argument = float(sys.argv[1])

            if argument.is_integer() and isinstance(argument,float):
                argument = int(argument)
            print(f"{argument * rate_float}")    
        except ValueError:
            pass
            return
    else:
        sys.exit(1)




main()