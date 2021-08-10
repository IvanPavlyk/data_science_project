# -*- coding: utf-8 -*-
import pandas as pd
import sys
from scipy import integrate

#Function that performs numerical integration using simpsons rule
def integration(array):
    return integrate.simps(array, x=None, dx=1, axis=-1, even='avg')

def difference(before, after):
    return abs(after-before)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    df = pd.read_csv(input_file)


    #Shift values of acceleration by 1 to get current and next values of acceleration side by side
    df['filtered_shifted'] = df['filtered'].shift(-1).fillna(0)

    #Integrate acceleration values to get velocity values
    df['velocity'] = df.apply(lambda row : integration([row['filtered'], row['filtered_shifted']]), axis = 1)
    #Shift values of velocity by 1 to get current and next values of velocities side by side
    df['velocity_shifted'] = df['velocity'].shift(-1).fillna(0)
    df.loc[df.index%32 == 0, 'velocity_shifted'] = 0



    #Integrate velocity values to get position values
    df['position'] = df.apply(lambda row : integration([row['velocity'], row['velocity_shifted']]), axis = 1)
    df = df.drop(['filtered_shifted', 'velocity_shifted'], axis=1)
    #Shift values of position by 1 to get current and next values of position side by side
    df['position_shifted'] = df['position'].shift(-1).fillna(0)
    df.loc[df.index%32 == 0, 'position_shifted'] = 0

    #Calculate distance travelled between two adjacent points by passing the values to difference function
    df['distance'] = df.apply(lambda row : difference(row['position'], row['position_shifted']), axis = 1)


    df_aggregate = df.groupby(['name', 'gender', 'collection type']).sum().reset_index()
    df_aggregate = df_aggregate[['name', 'distance']]
    df_aggregate = df_aggregate.rename(columns={'distance' : 'total_distance'})
    df_final = df.merge(df_aggregate, on='name')

    #Calculate average walking speed by dividing total distance travelled by total time travelled
    df_final['average walking speed'] = df_final['total_distance']/30
    df_final.to_csv(output_file, index=False)


if __name__ == '__main__':
    main()

