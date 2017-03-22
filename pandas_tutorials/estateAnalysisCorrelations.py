import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl

style.use('ggplot')


# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()


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


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={'Value': 'United States'}, inplace=True)
    df["United States"] = (df["United States"]-df["United States"][0]) / df["United States"][0] * 100.0
    return df


# grab_initial_state_data()

# fig = plt.figure()
# ax1 = plt.subplot2grid((1, 1), (0, 0))

# HPI_data = pd.read_pickle('fiddy_states_pct.pickle')
# benchmark = HPI_Benchmark()
#
# HPI_data.plot(ax=ax1)
# benchmark.plot(ax=ax1, color='k', linewidth=10)
#
# plt.legend().remove()
# plt.show()


HPI_data = pd.read_pickle('fiddy_states.pickle')
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())
