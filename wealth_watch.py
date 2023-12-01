import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


#We structured the code based on Objective Oriented Programing, using PortfolioAnalyzer as a class 
#with different methods that allow us perform operations with the main attributes of the class : tickers, dates, and weights
class PortfolioAnalyzer:
    def __init__(self, tickers, start_date, end_date, weights=None):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.weights = weights
        self.data = self.download_data()

#This method allow us to extract the data from yahoo finance, foccused on the column of the Adjusted Close Price
    def download_data(self):
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
        return data

#This method allow us to vizualize the historical stock prices
    def visualize_stocks(self):
        for ticker in self.data.columns:
            plt.plot(self.data.index, self.data[ticker], label=ticker)
        plt.title('Historical Stock Prices')
        plt.xlabel('Date')
        plt.ylabel('Adj. Close Price')
        plt.legend()
        plt.show()

#This method calculates the daily stock returns
    def calculate_daily_returns(self):
        stock_prices = self.data.values
        daily_returns = []
#We create forst an empty array in which then we will append the daily stock prices of each stock
        for i in range(1, len(stock_prices)):
            start_price = stock_prices[i - 1]
            end_price = stock_prices[i]
            daily_return = (end_price - start_price) / start_price
            daily_returns.append(daily_return)
#WThe provided code iterates the list of stock prices
#It calculates the daily return for each day by comparing today's price with yesterday's price.
#Then, the returns of the stock are given by the difference of the price divided by the starting price 
#Finally, it appends the calculated daily returns to a daily_returns list
        return pd.Series(daily_returns, index=self.data.index[1:])

#This method calculates the concrete return of each stock
#The return of each stock is obtained by computing the average returns (that is, the mean of the daily returns)
    def stock_returns(self):
        daily_returns = self.calculate_daily_returns()
        returns = pd.Series(daily_returns, index=self.data.index[1:])
        stock_returns = returns.mean()

        return stock_returns

#This method computes the portfolio return by computing the sum product of the stock returns and its corresponding weights in the portfolio
    def calculate_portfolio_return(self):
        stock_returns = self.stock_returns()
        portfolio_return = (stock_returns * self.weights).sum()

        return portfolio_return

    def calculate_statistics(self):#In this function the code calculates the Std of returns, the mean returns, and the correlation matrix
        daily_returns = self.data.pct_change().dropna()
        #The function uses allready in-build python fucntions
        mean_returns = daily_returns.mean()
        std_returns = daily_returns.std()
        correlation_matrix = daily_returns.corr()

        return {
            'average_returns': mean_returns,
            'std_returns': std_returns,
            'correlation_matrix': correlation_matrix,
        }

#Finaly, this method allow us to print a brief summary of the main results obtained from the portfolio (stoocks and the portfolio itself)
    def print_summary(self):

        print("\nReturns for Each Stock:")
        print(self.stock_returns())

        print("\nPortfolio Return:")
        print(self.calculate_portfolio_return())

        print("\nAverage Returns:")
        print(self.calculate_statistics()['average_returns'])

        print("\nStandard Deviations of Returns:")
        print(self.calculate_statistics()['std_returns'])

        print("\nCorrelation Matrix:")
        print(self.calculate_statistics()['correlation_matrix'],end='\n\n')


    def recommendations(self):#In this function the main objective is to get recommendations for the user portfolio
        stats = self.calculate_statistics()

        avg_returns = stats['average_returns']
        std_returns = stats['std_returns']

        corr_matrix = stats['correlation_matrix']
        recommendation_made = False #We build this variable to know if the code has identified a recommendation
        #In this for loop we check all the correlations between the tickers
        for i in range(len(corr_matrix)):
            for j in range(i + 1, len(corr_matrix)):
                corr = corr_matrix.iloc[i, j]

                if corr > 0.75:#If a correlation is over 0.75 we indentify between wich tickers it is.
                    recommendation_made = True

                    ticker1 = corr_matrix.index[i]
                    ticker2 = corr_matrix.columns[j]

                    avg_return1 = avg_returns[ticker1]
                    avg_return2 = avg_returns[ticker2]
                     #Depending in the avg_return the tickers have the program recommends if they user should sell one or thi other.
                    if avg_return1 > avg_return2:#
                        print(f"The stocks {ticker1} and {ticker2} have a high correlation of {corr:.2f}.")
                        print(f"The average return of {ticker1} is {avg_return1:.2%}, which is higher than the average return of {ticker2} ({avg_return2:.2%}).")
                        print(f"You may want to sell {ticker2} and keep {ticker1}.\n")
                    elif avg_return1 < avg_return2:
                        print(f"The stocks {ticker1} and {ticker2} have a high correlation of {corr:.2f}.")
                        print(f"The average return of {ticker2} is {avg_return2:.2%}, which is higher than the average return of {ticker1} ({avg_return1:.2%}).")
                        print(f"You may want to sell {ticker1} and keep {ticker2}.\n")
                    else:
                        print(f"The stocks {ticker1} and {ticker2} have a high correlation of {corr:.2f}.")
                        print(f"The average return of both stocks is {avg_return1:.2%}.")
                        print(f"You may want to sell one of them based on other factors.\n")
        #Here we check the std of stocks to see if they are too risky.
        for ticker in std_returns.index:#
            std = std_returns[ticker]

            if std > 0.03: #If the std of any of the tickers is higher than 0.03, we make a recommendation to sell that ticker as it is too volatile.
                recommendation_made = True
                avg_return = avg_returns[ticker]

                print(f"The stock {ticker} has a high standard deviation of {std:.2f}, which indicates a high risk.")
                print(f"The average return of {ticker} is {avg_return:.2%}.")
                print(f"If you are looking for a portfolio with less risk you may want to sell {ticker} and invest in a less volatile stock.\n")

        if not recommendation_made: #If the variable has not been updated to TRUE we conclude that the portfolio is ok.
            print("Your portfolio looks okay. No recommendations to make at this time.However you may want to look at other factors rather than just std and correlation.")
#USERS INPUT
tickers = input("Enter tickers separated by commas(In capital letters please): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
weights = input("Enter weights separated by commas: ")

if weights:
    weights = [float(w) for w in weights.split(',')]
    assert len(weights) == len(tickers.split(',')), "Number of weights must match number of tickers"
else:
    weights = None
#RUNING OF THE CODE
portfolio_analyzer = PortfolioAnalyzer(tickers, start_date, end_date, weights)

daily_returns = portfolio_analyzer.calculate_daily_returns()
stock_returns = portfolio_analyzer.stock_returns()
portfolio_return = portfolio_analyzer.calculate_portfolio_return()
statistics_result = portfolio_analyzer.calculate_statistics()
portfolio_analyzer.visualize_stocks()
portfolio_analyzer.print_summary()
portfolio_analyzer.recommendations()
