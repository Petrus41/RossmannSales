###############################################################################
# File:         utils.py
# Author:       Pierre Lasbleis
# Description:  Contains the function to process the dataset.
###############################################################################


import numpy as np

"""
Function loadStoreInfo()
Produce a list of entries containing the store information

Argument: 
* url_csv: a string containing the location of a csv file with one header line 
and the folowing fields: 
    * Store: integer
    * StoreType: char
    * Assortment: char
    * CompetitionDistance: integer
    * CompetitionOpenSinceMonth:integer
    * CompetitionOpenSinceYear: integer
    * Promo2: integer
    * Promo2SinceWeek: integer
    * Promo2SinceYear: integer
    * PromoInterval: string
    
Returns: 
    * data: a list. Each element is a list containing the fields as int 
    or string. 
"""
def loadStoreInfo(url_csv):
    ########################################
    # Local function to parse int to string 
    # and returns -1 if the string is empty
    ########################################
    def localParserInt(str):
        if len(str) > 0:
            return int(str)
        else:
            return -1
    ################## End of local function
    
    # Read file content
    content = -1
    with open(url_csv, 'r') as fid:
        content = fid.read()

    if content == -1:   # If the file is empty
        return []
    else:               # If the file is not empty

        data = list()
        lines = content.split('\n')[1:-1]
        for l in lines:
            fields = l.split(',')
            data.append( [
                localParserInt(fields[0]),      # Store
                fields[1][1:-1],                # StoreType, string 
                fields[2][1:-1],                # Assortment
                localParserInt(fields[3]),      # CompetitionDistance
                localParserInt(fields[4]),      # CompetitionOpenSinceMonth
                localParserInt(fields[5]),      # CompetitionOpenSinceYear
                localParserInt(fields[6]),      # Promo2
                localParserInt(fields[7]),      # Promo2SinceWeek
                localParserInt(fields[8]),      # Promo2SinceYear
                fields[9][1:-1]                 # PromoInterval
                ])
        return data

    

if __name__ == "__main__":
    print(loadStoreInfo("store.csv")[0])
