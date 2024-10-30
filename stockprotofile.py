import yfinance as yf

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, ticker):
        stock_data = yf.download(ticker, start='2020-01-01', end='2022-02-26')
        self.stocks[ticker] = stock_data

    def remove_stock(self, ticker):
        del self.stocks[ticker]

    def calculate_portfolio_value(self):
        total_value = 0
        for stock in self.stocks.values():
            total_value += stock['Adj Close'][-1]
        return total_value

    def track_performance(self):
        for stock in self.stocks.values():
            print(f"{stock['Adj Close'][-1]} ({stock['Adj Close'][-1] - stock['Adj Close'][0]})")

portfolio = Portfolio()
portfolio.add_stock('AAPL')
portfolio.add_stock('GOOG')
print(portfolio.calculate_portfolio_value())
portfolio.track_performance()
