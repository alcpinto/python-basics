import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    return stock_data


def plotGraph(x, y, marker='-', label=''):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    ax1.plot_date(x, y, marker, label=label)
    for l in ax1.xaxis.get_ticklabels():
        l.set_rotation(45)
    ax1.grid(True, color='gray')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

data = graph_data('TSLA')
date, closep, highp, lowp, openp, volume = np.loadtxt(data,
                                                    delimiter=',',
                                                    unpack=True)

dateconv = np.vectorize(dt.datetime.fromtimestamp)
date = dateconv(date)

plotGraph(date, closep, label='Price')
