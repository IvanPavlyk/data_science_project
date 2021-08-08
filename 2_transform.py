# -*- coding: utf-8 -*-
import pandas as pd
import sys
import glob
import names
from scipy import signal
import matplotlib.pyplot as plt

def main():
    input_file = "combined_data.csv"
    #output_file = sys.argv[2]
    output_file = "tranformed_data.csv"
    
    df = pd.read_csv(input_file)
    
    print(df)
    #frame = pd.concat(li, axis=0, ignore_index=True)
    #frame.to_csv(output_file, index=False)
    

if __name__ == '__main__':
    main()

