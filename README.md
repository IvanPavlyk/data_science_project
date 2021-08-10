Required libraries:
    - sys
    - glob
    - names
    - scipy
    - matplotlib
    - pandas
    - numpy
    
1. After downloading the project zip file, extract it into the folder of choice.

2. Assuming the project directory structure is unaltered, please follow these execution commands in order:
    1_extract.py:
        python3 1_extract.py data/ combined_data.csv
        Running 1_extract.py will produce combined_data.csv file which will serve as input in the next step.
    
    2_transform_load.py:
        python3 2_transform_load.py combined_data.csv tranformed_data.csv
        Running 2_transform_load.py will produce transformed_data.csv file 
        which will serve as input for the next step.
             
    3_analyze_data.py:
        python3 3_analyze_data.py tranformed_data
        Find meaningful relationships between age/height/gender/phone-position vs walking speed.
        Will produce a plot png file for each.
  
