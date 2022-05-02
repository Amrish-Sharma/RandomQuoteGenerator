import requests,json,random

quote_url='https://raw.githubusercontent.com/Amrish-Sharma/FlipQuotes/83e1820ff6c33f17a7f9312389a45ff04e0917d1/app/src/main/assets/quotes.json'

def rqg():
    response=requests.get(quote_url).json()
    response_json=response['quotes']
    random_quote=random.choice(response_json)
    print(random_quote)


def main():
    rqg()

if __name__ == "__main__":
    main()