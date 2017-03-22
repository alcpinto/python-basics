import pandas as pd
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce Rate': [65, 67, 78, 65, 45, 52]}

df = pd.DataFrame(web_stats)

# returns a new dataframe
# df2 = df.set_index('Day')
# print(df)

# change existing dataframe
df.set_index('Day', inplace=True)
print(df)


# print(df)
# print(df.head())
# print(df.head(3))
# print(df.tail())
# print(df.tail(2))

# similar statements to refer columns
# columns names with spaces are only allowed with first syntax
print(df['Visitors'])
print(df.Visitors)

# refer several columns
print(df[['Visitors', 'Bounce Rate']])

#  convert result to list
print(df.Visitors.tolist())
#  convert result to array if multi columns
print(np.array(df[['Visitors', 'Bounce Rate']]))

df3 = pd.DataFrame(np.array(df[['Visitors', 'Bounce Rate']]))
print(df3)

