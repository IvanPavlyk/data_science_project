Required libraries:
    - sys
    - glob
    - names
    - scipy
    - matplotlib
1. At first we take initial files and we want to extract useful info
and prepare for transformation.
2. First, run the 1_extract.py like this:
    - python3 1_extract.py C:\Users\vpavl\CMPT353\project\data combined_data.csv
    The argv[2] in this case corresponds to the absolute path of the data folder,
    this one will be different for the person running this code, change it
    accordingly
3. Running 1_extract.py will produce combined_data.csv file which will serve
as input in the next step.
4. Second, run the 2_transform_load.py like this:
    - python3 2_transform_load.py combined_data.csv tranformed_data.csv
5. Running 2_transform_load.py will produce transformed_data.csv file 
which will serve as input for the next step.
    

