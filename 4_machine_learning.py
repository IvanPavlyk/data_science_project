import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    # Check to see if data is normally distributed
    plt.hist(data['average walking speed'])
    data['age'] = np.float64(data['age'])
    print(data.dtypes)

    X = data[['age']]
    y = data['average walking speed']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    age_bayes_model = make_pipeline(
        StandardScaler(),
        GaussianNB()
    )
    #age_bayes_model.fit(X_train, y_train)
    #print("age_bayes_model: ", age_bayes_model.score(X_valid, y_valid))
    #print("age")


if __name__ == '__main__':
    main()
