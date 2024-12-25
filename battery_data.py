import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

dsets_path = r'C:\Users\Edward Korir\Documents\battery data'
dset_months = ['sep','oct','nov','dec']

all_data = pd.DataFrame()
for file in os.listdir(os.path.join(dsets_path, 'nov')):
    try:
        all_data = all_data.append(pd.read_csv(os.path.join(os.path.join(dsets_path, 'nov'), file), error_bad_lines=False))
    except Exception as e:
        print('nov', file, e)
    #print(pd.read_csv(os.path.join(os.path.join(dsets_path, month), file))))

all_data.to_csv(r'C:\Users\Edward Korir\Documents\nov_battery.csv', index=False)