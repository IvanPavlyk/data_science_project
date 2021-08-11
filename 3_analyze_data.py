import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats
import sys


def age_walking_speed(data):
    middle_aged = data[data['age'] > 40]
    young_adults = data[(data['age'] < 40) & (data['age'] > 18)]
    children = data[data['age'] < 18]
    print("\nMiddle_aged Avg Walking Speed: ", middle_aged['position_shifted'].mean())
    print("Young_adults Avg Walking Speed: ", young_adults['position_shifted'].mean())
    print("Children Avg Walking Speed: ", children['position_shifted'].mean())

    # Plot for different age groups
    plt.figure(figsize=(10, 5))
    plt.title("Walking Speed For Different Age Groups")
    plt.scatter(middle_aged['time_stamp'], middle_aged['position_shifted'], color='red', label='Middle-Aged')
    plt.scatter(young_adults['time_stamp'], young_adults['position_shifted'], color='green', label='Young Adult')
    plt.scatter(children['time_stamp'], children['position_shifted'], color='blue', label='Children')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("age_walking_speed.png")

    # Question: Does walking speed differentiate between age?
    age_anova = stats.f_oneway(middle_aged['position_shifted'], young_adults['position_shifted'],
                               children['position_shifted'])
    print("The ANOVA p-value for age groups: ", age_anova.pvalue)
    if age_anova.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between different age groups.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between different age groups.")


def gender_walking_speed(data):
    male = data[data['gender'] == 'male']
    female = data[data['gender'] == 'female']
    print("\nMale Avg Walking Speed: ", male['position_shifted'].mean())
    print("Female Avg Walking Speed: ", female['position_shifted'].mean())

    # Plot for male vs female
    plt.figure(figsize=(10, 5))
    plt.title("Walking Speed For Different Gender")
    plt.scatter(male['time_stamp'], male['position_shifted'], color='red', label='Male')
    plt.scatter(female['time_stamp'], female['position_shifted'], color='green', label='Female')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("gender_walking_speed.png")

    # Question: Does walking speed differentiate between gender?
    gender_ttest = stats.f_oneway(male['position_shifted'], female['position_shifted'])
    print("The Student's T-test p-value for male vs female: ", gender_ttest.pvalue)
    if gender_ttest.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between male vs female.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between male vs female.")


def height_walking_speed(data):
    height_below_140 = data[data['height'] < 140]
    height_140_to_170 = data[(data['height'] > 140) & (data['height'] < 170)]
    height_over_170 = data[data['height'] > 170]
    print("\nHeight_below_140cm Avg Walking Speed: ", height_below_140['position_shifted'].mean())
    print("Height_140_to_170cm Avg Walking Speed: ", height_140_to_170['position_shifted'].mean())
    print("Height_over_170cm Avg Walking Speed: ", height_over_170['position_shifted'].mean())

    # Plot for height
    plt.figure(figsize=(10, 5))
    plt.title("Walking Speed For Different Height Groups")
    plt.scatter(height_below_140['time_stamp'], height_below_140['position_shifted'], color='red',
                label='Height: < 140cm')
    plt.scatter(height_140_to_170['time_stamp'], height_140_to_170['position_shifted'], color='green',
                label='Height: 140~170')
    plt.scatter(height_over_170['time_stamp'], height_over_170['position_shifted'], color='blue',
                label='Height: > 170cm')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("height_walking_speed.png")

    # Question: Does walking speed differentiate between height?
    height_anova = stats.f_oneway(height_below_140['position_shifted'], height_140_to_170['position_shifted'],
                                  height_over_170['position_shifted'])
    print("The ANOVA p-value for height groups: ", height_anova.pvalue)
    if height_anova.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between different height groups.")
    else:
        print("We CANNOT conclude that there is a difference in walking speed between different height groups.")


def phone_pos_walking_speed(data):
    ankle = data[data['collection type'] == 'ankle']
    pocket = data[data['collection type'] == 'pocket']
    print("\nPhone-at-ankle Avg Walking Speed: ", ankle['position_shifted'].mean())
    print("Phone-in-pocket Avg Walking Speed: ", pocket['position_shifted'].mean())
    # Plot for male vs female
    plt.figure(figsize=(10, 5))
    plt.title("Walking Speed For Phone Position During Data Collection")
    plt.scatter(ankle['time_stamp'], ankle['position_shifted'], color='blue', label='Phone-at-ankle')
    plt.scatter(pocket['time_stamp'], pocket['position_shifted'], color='orange', label='Phone-in-pocket')
    plt.xlabel('Time (s)')
    plt.ylabel('Walking Speed (cm/s)')
    plt.legend()
    plt.savefig("phone_pos_walking_speed.png")

    # Question: Does walking speed differentiate between gender?
    phone_pos_ttest = stats.f_oneway(ankle['position_shifted'], pocket['position_shifted'])
    print("The Student's T-test p-value for phone-at-ankle vs phone-in-pocket: ", phone_pos_ttest.pvalue)
    if phone_pos_ttest.pvalue < 0.05:
        print("We CAN conclude that there is a difference in walking speed between phone-at-ankle vs phone-in-pocket.")
    else:
        print(
            "We CANNOT conclude that there is a difference in walking speed between phone-at-ankle vs phone-in-pocket.")


def main():
    data = pd.read_csv(sys.argv[1])
    age_walking_speed(data)
    gender_walking_speed(data)
    height_walking_speed(data)
    phone_pos_walking_speed(data)


if __name__ == '__main__':
    main()
