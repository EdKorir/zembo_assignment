# zembo_assignment
Battery Data Scientist Assignment

## The goal is to analyze battery data and swap data

### Requirements
pandas == 1.5.3

matplotlib == 3.8.0

seaborn == 0.13.2

numpy == 1.24.3

scipy == 1.10.0

scikit-learn == 1.1.3

adtk == 0.6.2

jupyter notebook == 7.0.8

Battery Data Analysis and Modelling.ipynb is the main notebook where all the analysis is done.
battery_data.py is the scripts that collects data from all the CSVs and creates one CSV for the month.

HTML version of the notebook has been added and can be viewed prior to running the notebook.

### Approach
Data was dumped as ZIP files within ZIP files. A script was written to read and aggregate all the data into 1 file for every month.
Due to size and memory limitations, data for the last 11 days of November was analyzed and explored to understand it’s inital structure.
From the EDA (exploatory data analysis) performed, data preparation steps were performed. These included removal of missing values, data type change and filling missing values, feature engineering etc.
The prepared data was then analyzed and used for modelling.

### Instructions to execute code
1. Install the packages under Requirements using: pip install <package == version>
2. Change the path under r'C:\Users\Edward Korir\Documents\nov_battery.csv' in cell 2 of the notebook to point to the data file (sent seperately)
3. Execute the notebook cell by cell.
