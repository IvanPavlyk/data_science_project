import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import stats
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
    middle_aged = data[data['age'] > 40]
    young_adults = data[(data['age'] < 40) & (data['age'] > 15)]
    children = data[data['age'] < 15]

    # Plot for different age groups
    plt.figure(figsize=(10,5))
    plt.title("Walking Speed For Different Age Groups")
    plt.scatter(middle_aged['time_stamp'], middle_aged['velocity'])
    plt.scatter(young_adults['time_stamp'], young_adults['velocity'])
    plt.scatter(children['time_stamp'], children['velocity'])
    plt.xlabel('Time')
    plt.ylabel('Walking Speed')
    plt.savefig("age_walking_speed.png")

    # Question: Does walking speed differentiate between age?
    age_anova = stats.f_oneway(middle_aged['velocity'], young_adults['velocity'], children['velocity'])
    print("The anova p-value: ", age_anova.pvalue)
    print("We conclude that there is a difference in walking speed between different age groups.")


if __name__ == '__main__':
    main()
