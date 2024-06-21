import pandas as pd

def webctrl_csv():
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

def metasys_csv():
    csv_file = 'metasys.csv'

    df = pd.read_csv(csv_file)

    # Define a function to extract the building number from the 'Item' column
    def extract_building_number(item):
        if "LBNL_EMS:" in item:
            return "EMS"
        elif "LBNL_FMS:" in item:
            return "FMS"
        else:
            # Extract the first sequence of 2 or more digits from the 'Item' string
            import re
            match = re.search(r'\b\d{2,}\b', item)
            if match:
                return match.group(0)
        return 'Unknown'

    # Apply the extraction function to the 'Item' column to create the 'Building' column
    df['Building'] = df['Item'].apply(extract_building_number)
    df['Vendor Name'] = 'Metasys'

    # Save the updated DataFrame back to a CSV file
    df.to_csv(csv_file, index=False)

# Call the function to update the CSV
metasys_csv()


# Tester