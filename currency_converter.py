import requests
API_KEY = "77f7791fc0679052b48129c0"            #free api-key from https://www.exchangerate-api.com/
BASE_URL = "https://v6.exchangerate-api.com/v6/"

def exchange_rate(API, from_cur, to_cur):
    url = f"{BASE_URL}{API}/pair/{from_cur}/{to_cur}"           #creating this URL because we're sending GET REQUEST
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:             #200 means Good
        return data["conversion_rate"]
    else :
        raise Exception(f"API Error: {data.get('error-type', 'Unknown Error')}")

def convert_cur():
    try:
        amount = float(input("Enter the amount you want to convert:- "))
        from_currency = input("Enter the 3-digit code of your currency:- ").upper()
        to_currency = input("Enter the 3-digit code of the currency in which you want to convert:- ").upper()
        rate = exchange_rate(API_KEY, from_currency, to_currency)
        amount_converted = amount * rate
        print(f"{amount} {from_currency}: {amount_converted:.2f} {to_currency}")
        print(f"1 {from_currency}= {rate:.6f} {to_currency}")
    except ValueError:
        print("Please enter the number.")
    except Exception as e:              #If this line is not written then it will show an ValueError for variables from_currency and to_currency.
        print(f"Error: {e}")

if __name__ == "__main__":              #Anything inside this code will be executed only when the script is run directly. It will not execute if it is imported as a module into another python file.
    convert_cur()