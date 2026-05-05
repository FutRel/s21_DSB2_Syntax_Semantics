import sys


def main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    company_ticker = sys.argv[1]

    for ticker, price in STOCKS.items():
        if ticker.lower() == company_ticker.lower():
            reverse_dict = {v: k for k, v in COMPANIES.items()}
            print(reverse_dict.get(ticker), " ", price)
            return

    print("Unknown company")


if __name__ == "__main__":
    main()
