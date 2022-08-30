import pickle
import numpy as np
import joblib
from sklearn.ensemble import GradientBoostingRegressor

# load the data and change the categorical fields to one hot encoding with replacement
def prepare_data(validated_data):

    with open('api/ml_model/columns.pkl', 'rb') as file:
        columns = pickle.load(file)

    for column in columns:
        columns[columns.index(column)] = str(column).replace("-", "_")
    columns.remove("price")
    data = np.zeros(len(columns))

    keys = list(validated_data.keys())
    for column in columns[:-3]:
        if column in keys:
            data[columns.index(column)] = validated_data[column]
            keys.remove(column)

    for key in keys:
        key += "_"+str(validated_data[key]).lower()
        if key in columns:
            data[columns.index(key)] = 1
    data = np.array(data)
    data = np.expand_dims(data, 0)

    return data


#load the model
def load_model(data):

    model = joblib.load('api/ml_model/model_gb.pkl')

    return model
