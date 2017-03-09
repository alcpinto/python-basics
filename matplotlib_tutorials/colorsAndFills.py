import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
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
    ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.3)
    ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.3)
    for l in ax1.xaxis.get_ticklabels():
        l.set_rotation(45)
    ax1.grid(True, color='gray')
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0, 25, 50, 75])

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('EBAY')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

data = graph_data('EBAY')
date, closep, highp, lowp, openp, volume = np.loadtxt(data,
                                                    delimiter=',',
                                                    unpack=True,
                                                    # %Y = full year. 2015
                                                    # %y = partial year 15
                                                    # %m = number month
                                                    # %d = number day
                                                    # %H = hours
                                                    # %M = minutes
                                                    # %S = seconds
                                                    # 12-06-2014
                                                    # %m-%d-%Y
                                                    converters={0: mdates.bytespdate2num('%Y%m%d')})
# print(date) date are in matplotlib format

plotGraph(date, closep, label='Price')
