import pandas as pd
import matplotlib

HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data['TX2'] = HPI_data['TX'] * 2
print(HPI_data[['TX', 'TX2']].head())
