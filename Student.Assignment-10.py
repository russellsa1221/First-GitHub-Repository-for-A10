import json
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

"""
Name: George Arias

Date: 03/13/2020

Description: This purpose of this program is to allow someone interested in stocks
to see to daily price percentages of various stocks. A Pie graph is shown to the user 
that shows the price percentages of every unique stock compared to each other.
A higher percentage means that the stock is worth a lot more than other stocks.
"""

#-CompanyStockOwned class
#-This class represents a unique stock that exists in the JSON file. 

class CompanyStockOwned():
    
    #-__init__ class
    #-This method intializes the CompanyStockOwned class with stock attributes.
    #-The attributes include the ompany stock data (or the stock
    #symbol), a list of the closing dates and a list of closing stock prices.
    #-The list of dates represent the date where the stock was valued at the
    #corresponding closing price found in the list of closing stock prices.
    
    def __init__(self, company_stock_data):
        self.company_stock_data = company_stock_data
        self.closing_dates = []
        self.closing_prices = []
    
    #-add_stock_price_and_date function
    #-Appends the closing date and closing price of the stock that is found in the 
    #JSON file.
    
    def add_stock_price_and_date(self, date, price):
        self.closing_dates.append(date)
        self.closing_prices.append(price)


#-Stock JSON data reading
#-A company_stocks dictionary is created to hold all of the different company stocks 
#that exist in the JSON file that will be loaded.
#-The stock_file_name string has the name of a local JSON file that has 
#stock information.

company_stocks = {}
stock_file_name = 'AllStocks.json'

#-The try/except blocks catch a FileNotFoundError exception, which occurs when
#you try to access a file that does not exist.

try:
    #-The JSON file is opened and all of its contents (stock information) 
    #are stored in a date_set dictionary.
    
    with open(stock_file_name) as stock_information:
        date_set = json.load(stock_information)
    
    #-For every piece of stock information in the date_set dictionary, if 
    #the stock symbol of that stock information does not exist in the company_stocks 
    #dictionary, the stock information is loaded into the company_stocks dictionary. 
    #-Otherwise, the stock information's date and closing price and appended to
    #the corresponding unique stock in the company_stocks dictionary.
    #-The date is formatted in a way that works with matplotlib.
    #%d stands for the day in the date. %b stands for the month in the date. %y stands for the year in the date.

    for stock_information in date_set:
        if stock_information['Symbol'] not in company_stocks:
            company_stocks[stock_information['Symbol']] = {'stock' : CompanyStockOwned(stock_information['Symbol'])}
        company_stocks[stock_information['Symbol']]['stock'].add_stock_price_and_date(datetime.strptime(stock_information['Date'], '%d-%b-%y'), int(stock_information['Close']))
       
    #-The matplotlib plot's dimensions are set. The DPI (Dots Per Inch) viewing 
    #resolution is set to 100 and the plotting window size is set to 16 by 10 inches.
    #-The title of the plot is "Stock Price Comparison" and the font size is 24.

    
    fig = plt.figure(dpi = 100, figsize = (16, 10))
    plt.title('Stock Price Comparison', fontsize = 24)
    
    #-A stock_prices array is created to hold the first closing price of a
    #particular stock within the company_stocks dictionary.
    
    stock_prices = [company_stocks['AIG']['stock'].closing_prices[0],
    company_stocks['F']['stock'].closing_prices[0],
    company_stocks['FB']['stock'].closing_prices[0],
    company_stocks['GOOG']['stock'].closing_prices[0],
    company_stocks['IBM']['stock'].closing_prices[0],
    company_stocks['M']['stock'].closing_prices[0],
    company_stocks['MSFT']['stock'].closing_prices[0],
    company_stocks['RDS-A']['stock'].closing_prices[0]]
    
    #-The plt.pie() method plots out the pie chart.
    #-The stock_prices parameter is the array of values for each unique stock.
    #-The colors parameter is the array that contains the colors of the actual pie slices
    #in the pie chart.
    #-The explode parameter is an array of float values that correspond to the 
    #stock_prices array and determine which slices on the pie chart will be offset
    #from the radius determined by the values in the explode array that are non-zero values.
    #-The autopct parameter is a string that will display the value of the stock as a percentage value.
    #-The shadow parameter determines whether there is a shadow effect under the pie chart.
    
    
    plt.pie(stock_prices, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple',
    'red', 'brown', 'orange'], explode = [0, 0, 0, 0.1, 0, 0, 0, 0], autopct='%1.2f%%', shadow=True)
    
    #-The plt.legend() method is used to display a legend for the pie chart.
    #-The labels parameter is an array of strings that will be the labels of the
    #stocks/slices in the pie chart.
    #-The fontsize parameter is an integer that is the font size of the labels on the legend.
    #-The loc parameter is a string that is used to place the legend in a particular place. 
    #-The value "best" is assigned to loc and places the legend in a place that does
    #not overlap the pie graph that much.
    #-The plt.axis() method with the "equal" string passed into it allows the pie
    #chart and legend to use up as much space in the plot that is created.
    #The plt.show() method outputs the pie chart to the user.
    
    plt.legend(labels=['AIG', 'F', 'FB', 'GOOG', 'IBM', 'M', 'MSFT', 'RDS-A'], fontsize = 15, loc = 'best')
    plt.axis('equal')
    plt.show()
       
except FileNotFoundError:
    print('Can not find the ' + stock_file_name + ' file.\n')

