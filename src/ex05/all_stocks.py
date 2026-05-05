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

    input_string = sys.argv[1]
    
    expressions = input_string.split(',')
    
    for expr in expressions:
        if not expr.strip():
            return
    
    results = []
    
    for expr in expressions:
        expr_clean = expr.strip()
            
        expr_upper = expr_clean.upper()
        expr_proper = expr_clean.title()
        
        if expr_upper in STOCKS:
            company_name = None
            for company, ticker in COMPANIES.items():
                if ticker == expr_upper:
                    company_name = company
                    break
            results.append(f"{expr_clean} is a ticker symbol for {company_name}")
        
        elif expr_proper in COMPANIES:
            ticker = COMPANIES[expr_proper]
            price = STOCKS[ticker]
            results.append(f"{expr_proper} stock price is {price}")
        
        else:
            results.append(f"{expr_clean} is an unknown company or an unknown ticker symbol")
    
    if results:
        print('\n'.join(results))


if __name__ == "__main__":
    main()