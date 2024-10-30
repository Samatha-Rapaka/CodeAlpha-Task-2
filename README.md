# CodeAlpha-Task4
Certainly! Let's break down the provided code step by step to understand its components and functionality.
<h2>1. Importing Libraries</h2>
<h3>yfinance:</h3> This library is used to fetch historical stock price data from Yahoo Finance.
<h3>pandas:</h3> A powerful data manipulation library that provides data structures like DataFrames for handling structured data.
<h3>numpy:</h3> A library for numerical operations, particularly useful for handling arrays and performing mathematical calculations.
<h3>matplotlib.pyplot:</h3> A plotting library used for creating static, animated, and interactive visualizations in Python.

<h2>2. Fetching Stock Data</h2>
<h3>Function: fetch_stock_data</h3> takes a list of stock tickers and a date range as input.
<h3>yfinance.download:</h3> This function fetches historical stock data for the specified tickers and date range.
<h3>Return Value:</h3> The function returns the adjusted close prices, which account for dividends and stock splits, making them more accurate for analysis.

<h2>3. Calculating Daily Returns</h2>
<h3>Function: calculate_daily_returns</h3> computes the daily returns of the stocks.
<h3>pct_change(): </h3>This method calculates the percentage change between the current and previous row, giving the daily return.
<h3>dropna():</h3> This method removes any rows with NaN values, which occur for the first row since there is no previous day to compare.

<h2>4. Portfolio Class</h2>
<h3></h3>Class: Portfolio encapsulates the concept of a stock portfolio.
Constructor (__init__): Initializes the portfolio with a list of assets (tickers) and their corresponding weights (proportions of the total investment).
Methods:
expected_return: Calculates the expected annual return of the portfolio by taking the dot product of the weights and the mean daily returns, then annualizing it by multiplying by 252 (the typical number of trading days in a year).
portfolio_volatility: Calculates the annualized volatility of the portfolio. It computes the covariance matrix of daily returns, calculates the portfolio variance using the weights, and then takes the square root to get the standard deviation (volatility).
