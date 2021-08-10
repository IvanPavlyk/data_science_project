# -*- coding: utf-8 -*-
import pandas as pd
import sys
import glob
import names
from scipy import signal
import matplotlib.pyplot as plt


def increment_count(count):
    return_count = count[0]
    count[0] += 1
    return return_count % 31


def main():
    li = [] # array of DataFrames
    path = sys.argv[1]
    output_file = sys.argv[2]
    all_files = glob.glob(path + "/*.csv")

    # Extract all the data from files and add to an array of DataFrames
    # Butter filtering and example plots of data before and after filtering
    b, a = signal.butter(3, 0.1, btype='lowpass', analog=False)
    count = [0]
    for filename in all_files:
        attributes = filename.split("_")
        attributes_gender = attributes[0].split("\\")
        attributes[0] = attributes_gender[len(attributes_gender) - 1]
        attributes[len(attributes) - 1] = attributes[len(attributes) - 1].strip('.csv')
        df = pd.read_csv(filename, index_col=None, header=0)
        df = df.drop(['ax'], axis=1)
        df = df.drop(['ay'], axis=1)
        df = df.drop(['az'], axis=1)
        df['name'] = names.get_first_name(gender=attributes[0])
        df['gender'] = attributes[0]
        df['age'] = int(attributes[1])
        df['height'] = int(attributes[2])
        df['collection type'] = attributes[3]
        df['time_stamp'] = df.apply(lambda row: increment_count(count), axis = 1)
        low_passed = signal.filtfilt(b, a, df['atotal'])
        df['filtered'] = low_passed
        df = df.drop(['time'], axis=1)
        li.append(df)


    for i in range(0,2):
        plt.figure(figsize=(10,5))
        title = "{}'s Acceleration Over Time".format(li[i]['name'][0])
        plt.title(title)
        plt.xlabel('Time (s)')
        plt.ylabel('Acceleration (m/s^2)')
        plt.plot(li[i]['time_stamp'], li[i]['atotal'], 'b-', label='Before Butterworth filter  ')
        plt.plot(li[i]['time_stamp'], li[i]['filtered'], 'r-', label = 'After Butterworth filter ')
        plt.legend()
        file_name = "{}_filtering.png".format(i)
        plt.savefig(file_name)

    frame = pd.concat(li, axis=0)
    frame.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()