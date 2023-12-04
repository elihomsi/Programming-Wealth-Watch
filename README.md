# Programming-Wealth-Watch
## Overview 

Wealth Watch is a Python application (run on console) designed for investors to measure the performance of their portfolio’s investments, and furthermore aims to help them to make intelligent decisions based on portfolio optimization recommendations provided by the app. 

## Features 

Download and Visualise Data : The program has a download data method that allow the user to directly collect data extracted from yahoo finance by using yfincance package in python. Following this sense, the visualise data method allows the user to plot each stock's historical prices.

Daily Stock Returns : This feature calculates each stock’s daily returns by using the historical data of the prices. These daily returns are calculated by using the formula Daily Returns = (Today's adjusted price - Yesterday's adjusted price)/Yesterday's adjusted price

Average Stock Returns : This feature calculates the concrete return of each stock. In this sense, the program computes the average stock returns by calculating the average from the daily returns. 

Portfolio Return : This feature calculates the portfolio return by computing Portfolio Return = w1*R1 + w2*R2 + ... + wn*Rn, where w is each stock’s weighting and R the returns of each stock.

Calculate Statistics (key metrics) : This feature calculates the main financial metrics to measure risk and return, and furthermore make recommendations based on these statistics. 

Performance Summary : This feature prints an overall summary of the portfolio’s performance and calculations.

Recommendation Generation : This feature generates actual recommendations for portfolio decision-taking based on the metrics’ calculations.


## How to Use
Install Python (in case is not installed)

Install the following packages on the Python Terminal : 
pip instal yfinance
pip instal pandas
pip instal matplotlib.pyplot

Run the python script (wealth_watch.py)

Input the the following requirements : 
Tickers from desired stocks (write them in upper case)
Start and End dates desired for the historical data
Portfolio weights for each corresponding stock (must follow the order of the tickers already written)

Explore the Stocks’ and Portfolio’s performance summary and the recommendations provided




## Sample Data
The program allows the user to create a sample data based on the requirements entered by the user (dates and tickers) extracted from Yahoo Finance dynamic data base.


## Dependencies 
The program only depends on the connection to the external data information stored in Yahoo Finance. 


## Notes
When asked to enter the stocks tickers, input them separated with commas. You may search in Yahoo Finance’s web to know the ticker assigned to each corresponding company. 
When asked to enter the dates (end and start dates), please follow this format : (YYYY-MM-DD)
When asked to enter the portfolio weights, note that it should be in terms of percentage. In this sense, enter weights from 0-1, separated by commas and following the same order of their corresponding stock to assign.
The program aims just to measure the actual portfolio performance and make recommendations over it. However, Wealth Watch is not capable of making predictive models or to make recommendations over future or estimated stocks performance; The main objective is to operate over actual performance based over historical stock data. 


## Future Improvements 
Advance on the development of future predictive models that allow the user to take decisions over the future performance of his/her portfolio.
Improve on the visuals and esthetic design of the app and of the tables provided in the output
Develop an user interface to improve the user experience when using the app


## Authors 
Eduardo Alfaro, Sergio Garcia, Felipe Gomez, Eli Homsi
