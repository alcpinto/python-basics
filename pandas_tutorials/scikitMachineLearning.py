import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, model_selection
style.use('ggplot')

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt', 'r').read()


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0


# Python already implements it. It's just to show how to apply custom functions
def moving_average(values):
    return mean(values)


housing_data = pd.read_pickle('HPI.pickle')
# Apply a change based on previous value
housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data.dropna(inplace=True)

housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)
# print(housing_data[['US_HPI_future', 'United States']].head())

housing_data['label'] = list(map(create_labels, housing_data['United States'], housing_data['US_HPI_future']))
print(housing_data.head())

X = np.array(housing_data.drop(['label', 'US_HPI_future'], 1))
X = preprocessing.scale(X)
y = np.array(housing_data['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
