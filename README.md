Required libraries:
    - import sys
    - import glob
    - import names
    - import scipy
    - import matplotlib
    - import pandas as pd
    - import numpy
    - import matplotlib.pyplot as plt
    - from scipy.stats import stats
    
1. After downloading the project zip file, extract it into the folder of choice.

2. Assuming the project directory structure is unaltered, please go to the project root directory and follow these execution commands in order:
    1_extract.py:

        $ python3 1_extract.py data/ combined_data.csv
        
        Running 1_extract.py will produce combined_data.csv file which will serve as input in the next step.
    
    2_transform_load.py:

        $ python3 2_transform_load.py combined_data.csv tranformed_data.csv
        
        Running 2_transform_load.py will produce transformed_data.csv file 
        which will serve as input for the next step.
             
    3_analyze_data.py:
    
        $ python3 3_analyze_data.py tranformed_data.csv
        
        Find meaningful relationships between age/height/gender/phone-position vs walking speed.
        Will produce a series of analysis and print the results.
        Will produce age_walking_speed.png, gender_walking_speed.png, height_walking_speed.png, phone_pos_walking_speed.png
  
