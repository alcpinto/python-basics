import pandas as pd

# df = pd.read_csv('ZILL-Z77006_3B.csv')
# print(df.head())

# df.set_index('Date', inplace=True)
# df.to_csv('newcsv2.csv')


# df = pd.read_csv('ZILL-Z77006_3B.csv', index_col=0)
# print(df.head())
#
# df.columns = ['Austin_HPI']
# print(df.head())
# df.to_csv('newcsv3.csv')
# df.to_csv('newcsv4.csv', header=False)
#
# df = pd.read_csv('newcsv4.csv', names=['date', 'austin_hpi'], index_col=0)
# print(df.head())
#
# df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['date', 'austin_hpi'])
print(df.head())

df.rename(columns={'austin_hpi': '77006_hpi'}, inplace=True)
print(df.head())

