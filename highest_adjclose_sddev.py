import datetime
import pandas as pd
import pandas.io.data

# Load the stocks codes from an external file
stocks_file = open('stocks_list.txt', 'r')
stocks_list = []

# Note: the stock market is closed on New Year's Day
start_date = datetime.datetime(2015, 1, 1)
end_date = datetime.datetime(2015, 9, 28)

# This dict has the current stock with the highest std
current_highest_adjclose = {'stock': 'placeholder', 'stdev': -1}

# Add the stocks to a new list while removing \n
for line in stocks_file:
    stocks_list.append(line.strip('\n'))

for stock in stocks_list:
    print stock
    try:
        s = pd.io.data.get_data_yahoo(stock, start=start_date,
                                      end=end_date)['Adj Close']
        current_standard_deviation = s.std()
        if current_standard_deviation > current_highest_adjclose['stdev']:
            current_highest_adjclose['stock'] = stock
            current_highest_adjclose['stdev'] = current_standard_deviation
    except:
        'Something happened with ', stock

print 'Highest \'Adj Close\' is: %f (%s)' % (
    current_highest_adjclose['stdev'],
    current_highest_adjclose['stock'])