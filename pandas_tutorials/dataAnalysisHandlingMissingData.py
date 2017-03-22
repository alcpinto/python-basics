import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl

style.use('ggplot')


# Not necessary, I just do this so I do not show my API key.
# api_key = open('quandlapikey.txt','r').read()
api_key = 'make program happy'

def state_list():
    # List of dataframes print(fiddy_states)
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()
    # Creates an empty dataframe
    main_df = pd.DataFrame()
    # Iterate over rows 1 to end (discard first row because is table headers)
    # of first column of first dataframe
    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        # df = df.pct_change()
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    # using pandas pickle implementation - fast for huge dataframes
    main_df.to_pickle('fiddy_states_pct.pickle')


def hpi_benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={'Value': 'United States'}, inplace=True)
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    return df


# grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fiddy_states.pickle')

# 'A' means Annual
# TX1yr = HPI_data['TX'].resample('A', how='ohlc')
# New syntax
HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
print(HPI_data[['TX', 'TX1yr']].head())
# Removes all rows that have NaN
# HPI_data.dropna(inplace=True)
# Removes all rows that have NaN in 'all' columns
# HPI_data.dropna(how='all', inplace=True)
# Fill all NaN with a specific value
# method='ffill' -> takes a previous value and fill forward with that value
# method='bfill' -> takes a forward value and fill backwards with that value
# value=-99999 -> Fills with the value passed in parameter.
# Very useful in machine learning because the model can interpreter as an outlier
# limit -> number of substitutions that we want to do
HPI_data.fillna(value=-99999, limit=10, inplace=True)
print(HPI_data[['TX', 'TX1yr']].head())

# Check how many rows NaN we have
print(HPI_data.isnull().values.sum())

HPI_data[['TX', 'TX1yr']].plot(ax=ax1)

plt.legend()
plt.show()
