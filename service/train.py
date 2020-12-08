from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import pickle
import os

model_local_path = os.environ.get('MODEL_LOCAL_PATH', "pickled_model.pkl")

data = load_wine()  # import dataset
df = pd.DataFrame(data['data'], columns=data['feature_names'])  # build dataframe
df['target'] = data['target']  # add dependent variable
df = df.sample(frac=1)  # randomize the data
df.head(3)

print("row count:", len(df))
train_df = df[:150]
test_df = df[150:]
# => row count: 178


def x_n_y_from_df(df, y_column, x_columns=[]):
    '''Extract data from the dataframe'''
    X = {}
    for feature in x_columns:
        X[feature] = df[feature].tolist()
    y = df[y_column].tolist()
    return X, y


x_train, y_train = x_n_y_from_df(train_df, 'target', ['alcohol'])
x_test, y_test = x_n_y_from_df(test_df, 'target', ['alcohol'])
x_train = np.array(x_train['alcohol']).reshape(-1, 1)
x_test = np.array(x_test['alcohol']).reshape(-1, 1)

model = LogisticRegression()
model.fit(x_train, y_train)

pickle.dump(model, open(model_local_path, "wb"))
