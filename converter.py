import requests


API_KEY = 'fca_live_hZ9WajClxFXpBQxRehlovxcKr8cfdJEek0td2jX5'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'EUR', 'CNY', 'JPY', 'RUB']


def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except :
        print('Currency ticker error.')
        return None


def main():
    base = input('Please enter a currency ticker, e.g. USD: ').upper()
    while True:
        try:
            amount = float(input('Please enter currency amount to exchange: '))
        except ValueError:
            print('You should enter a valid amount.\n')
        else:
            break

    data = convert_currency(base)

    if data:
        del data[base]
        for key, value in data.items():
            print(f'{key}: {value * amount}')
    input('Press ENTER to exit.')


if __name__ == '__main__':
    main()
