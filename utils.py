###############################################################################
# File:         utils.py
# Author:       Pierre Lasbleis
# Description:  Contains the function to process the dataset.
###############################################################################


import numpy as np


def loadStoreInfo(url_csv):
    # Read file content
    content = -1
    with open(url_csv, 'r') as fid:
        content = fid.read()

    if content == -1:
        return []
    else:

        data = list()
        lines = content.split('\n')[1:-1]
        for l in lines:
            fields = l.split(',')
            data.append( [
                int(fields[0]),     # Store
                fields[1][1:-1],    # StoreType, string 
                fields[2][1:-1],    # Assortment
                int(fields[3]),     # CompetitionDistance
                int(fields[4]),     # CompetitionOpenSinceMonth
                int(fields[5]),     # CompetitionOpenSinceYear
                int(fields[6]),     # Promo2
                int(fields[7]),     # Promo2SinceWeek
                int(fields[8]),     # Promo2SinceYear
                fields[9][1:-1]     # PromoInterval
                ])
        return data

    

if __name__ == "__main__":
    print(loadStoreInfo("store.csv"))
