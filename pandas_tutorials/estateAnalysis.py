#  Before install quandl
# sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev

import quandl
import pandas as pd
import pickle


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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())
    # wb means write bytes
    # pickle_out = open('fiddy_states.pickle', 'wb')
    # pickle.dump(main_df, pickle_out)
    # pickle_out.close()

    # using pandas pickle implementation - fast for huge dataframes
    main_df.to_pickle('fiddy_states.pickle')


# grab_initial_state_data()
# pickle_in = open('fiddy_states.pickle','rb')
# HPI_data = pickle.load(pickle_in)
# pickle_in.close()

# using pandas pickle implementation
HPI_data = pd.read_pickle('fiddy_states.pickle')
print(HPI_data)
