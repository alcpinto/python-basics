#  Before install quandl
# sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev

import quandl
import pandas as pd

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()
# df = quandl.get("FMAC/HPI_TX", authtoken=api_key)
#
# print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states)

for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_'+abbv)
