import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats
import sys


def age_walking_speed(data):
    middle_aged = data[data['age'] > 40]
    young_adults = data[(data['age'] < 40) & (data['age'] > 15)]
    children = data[data['age'] < 15]
    print("\nMiddle_aged avg velocity: ", middle_aged['velocity'].mean())
    print("\nYoung_adults avg velocity: ", young_adults['velocity'].mean())
    print("\nChildren avg velocity: ", children['velocity'].mean())

    # Plot for different age groups
    plt.figure(figsize=(10,5))
    plt.title("Walking Speed For Different Age Groups")
    plt.scatter(middle_aged['time_stamp'], middle_aged['velocity'], color = 'blue', label='Middle-Aged')
    plt.scatter(young_adults['time_stamp'], young_adults['velocity'], color = 'red', label='Young Adult')
    plt.scatter(children['time_stamp'], children['velocity'], color = 'green', label='Children')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("age_walking_speed.png")

    # Question: Does walking speed differentiate between age?
    age_anova = stats.f_oneway(middle_aged['velocity'], young_adults['velocity'], children['velocity'])
    print("\nThe anova p-value for age groups: ", age_anova.pvalue)
    if age_anova.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between male vs female.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between male vs female.")


def gender_walking_speed(data):
    male = data[data['gender'] == 'data/male']
    female = data[data['gender'] == 'data/female']
    # check correct extracted groups
    # print(male)
    # print(female)
    print("\nMale avg velocity: ", male['velocity'].mean())
    print("\nFemale avg velocity: ", female['velocity'].mean())

    # Plot for male vs female
    plt.figure(figsize=(10,5))
    plt.title("Walking Speed For Different Age Groups")
    plt.scatter(male['time_stamp'], male['velocity'], color='red', label='Male')
    plt.scatter(female['time_stamp'], female['velocity'], color='green', label='Female')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("gender_walking_speed.png")

    # Question: Does walking speed differentiate between gender?
    gender_ttest = stats.f_oneway(male['velocity'], female['velocity'])
    print("\nThe Student's t-distribution p-value for male vs female: ", gender_ttest.pvalue)
    if gender_ttest.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between male vs female.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between male vs female.")


def height_walking_speed(data):
    # Plot for height
    plt.figure(figsize=(10,5))
    plt.title("Walking Speed For Different Height")
    plt.scatter(data['height'], data['velocity'])
    plt.xlabel('Height (m)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.savefig("height_walking_speed.png")

    reg = stats.linregress(data['height'], data['velocity'])
    print("\nRegression p-value for height vs Walking Speed", reg.pvalue)
    if reg.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between people of different height.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between people of different height.")



def main():
    data = pd.read_csv(sys.argv[1])
    age_walking_speed(data)
    gender_walking_speed(data)
    height_walking_speed(data)


if __name__ == '__main__':
    main()
