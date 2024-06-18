import pandas as pd

csv_file = 'webctrl.csv'

df = pd.read_csv(csv_file)

# selected location
df_loc = df[['Location']]

# to locate the index of the starting of the building number
def find_nth_occurrence(string, char, n):
    occurrence = -1
    for i in range(n):
        occurrence = string.find(char, occurrence + 1)
        if occurrence == -1:
            return -1  # Return -1 if the character is not found enough times
    return occurrence

df['Building'] = 'Unknown' # added building col
# used to find the building number of the controller
# will be added to csv file
for index in range(0, len(df_loc)):
    row = df_loc.at[index, 'Location']  # df_loc.at[x, 'Location'] accesses the value in the 'Location' column for each row
    start = find_nth_occurrence(row, '/', 5) # index start of building number
    start += 1
    end = start + 2

    # adds building number to each row
    if start != 0: # orignal is -1, but compensated due to incremented start
       bld_num = row[start:end]
       df.__getitem__('Building').__setitem__(index, bld_num)
df.to_csv(csv_file, index=False)