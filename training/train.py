from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import pickle
import os

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

data = load_wine() # import dataset
df = pd.DataFrame(data['data'], columns=data['feature_names']) # build dataframe
df['target'] = data['target'] # add dependent variable
df = df.sample(frac=1) # randomize the data
df.head(3)

print("row count:",len(df))
train_df = df[:150]
test_df = df[150:]
#=> row count: 178

def X_and_y_from_df(df, y_column, X_columns = []):
    '''Extract data from the dataframe'''
    X = {}
    for feature in X_columns:
        X[feature] = df[feature].tolist()
    y = df[y_column].tolist()
    return X, y
X_train, y_train = X_and_y_from_df(train_df, 'target', ['alcohol'])
X_test, y_test = X_and_y_from_df(test_df, 'target', ['alcohol'])
X_train = np.array(X_train['alcohol']).reshape(-1,1)
X_test = np.array(X_test['alcohol']).reshape(-1,1)

model = LogisticRegression()
model.fit(X_train, y_train)

pickle.dump( model, open( MODEL_DIR+"/pickled_model.p", "wb" ) )
