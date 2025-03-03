"""
This conversts ACS income tables grouped by year a single csv file containing information for all the state
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

find_state = lambda str : str[:str.index("!")] if '!' in str else str
mystring_to_int = lambda str : int(str.replace(',',''))
mypercent_to_float = lambda str : float(str.replace('%',''))/100 if '%' in str else 0


def get_dataset_by_year(year):
     # grabs the data until the mean and median income
    df = pd.read_csv(f'.\\..\\data\\acs_income_by_year\\acs_income_{year}.csv')
    df = df.iloc[:11]
    #find all the states
    USstates = {find_state(col) for col in df.columns[1:]}
    USstates = list(USstates)
    USstates.sort()
    #prepare new dataframe and keep the income braket labels
    df2 = pd.DataFrame()
    df2['label'] = [str.replace(u'\xa0','') for str in df['Label (Grouping)']]
    # construct dataframe grouped by state
    for us_state in USstates:
        get_columns_for_state = [x for x in df.columns if find_state(x) == us_state]
        state_list = []
        counts = [mystring_to_int(x) for x in df.iloc[0][get_columns_for_state]]
        state_list.append(sum(counts))
        row_ind = 0
        for row in np.array(df.iloc[1:][get_columns_for_state]): 
            row_ind+=1
            new_row_sum = 0
            for ind in range(len(get_columns_for_state)):
                new_row_sum+=int(mypercent_to_float(row[ind])*counts[ind])
            state_list.append(new_row_sum)
        df2[us_state] = state_list
    df2['Year'] = [year for _ in state_list]
    return df2

YEARS = [2010 +j for j in range(14) if j !=10]
df_list = [get_dataset_by_year(year) for year in YEARS]
total_df = pd.concat(df_list)

total_df.to_csv(".\\..\\data\\acs_income_by_year\\all_income_from_2010_to_2023.csv")
