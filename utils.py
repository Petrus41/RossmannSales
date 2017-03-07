###############################################################################
# File:         utils.py
# Author:       Pierre Lasbleis
# Description:  Contains the function to process the dataset.
###############################################################################


import numpy as np
from datetime import date

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
        lines = content.split('\n')[1:-1] # Skip header and last (empty) line
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

        
        
"""
Function loadTrainingData()
Produce a list of entries containing the training data and the outputs. 

Argument: 
* url_csv: a string containing the location of a csv file with one header line 
and the folowing fields: 
    * Store: Integer
    * DayOfWeek: Integer
    * Date: date
    * Sales: Integer
    * Customers: Integer
    * Open: Integer
    * Promo: Integer
    * StateHoliday: char
    * SchoolHoliday: char
    
Returns: 
    * data: a list. Each element is a list containing the fields as int 
    or char or datetime
    * output_sales: list
    * output_customers: list
"""
def loadTrainingData(url_csv):
    
    # Load file
    content = -1
    with open(url_csv, 'r') as fid:
        content = fid.read()
        
    if content == -1:   # empty file or reading problem    
        return [],[],[]
    else:               # File read
        data = list()
        output_sales = list()
        output_customers = list()
    
        lines = content.split('\n')[1:-1] # Skip header and last (empty) line
        for l in lines:
            fields = l.split(',')
            
            # Read fields
            output_sales.append(int(fields[3]))
            output_customers.append(int(fields[4]))
            data.append([
                int(fields[0]), # Store id
                int(fields[1]), # Day of week
                date(
                    int(fields[2][:4]),     # Year 
                    int(fields[2][5:7]),    # Month
                    int(fields[2][8:10])),  # Day
                int(fields[5]), # Open
                int(fields[6]), # Promo
                fields[7][1],   # StateHoliday
                fields[8][1]    # SchoolHoliday
                ])
                
        return data, output_sales, output_customers

if __name__ == "__main__":
    print(loadStoreInfo("store.csv")[0])
    
    (input, output_sales, output_customers) = loadTrainingData("train.csv")
    
    print(input[0])
    print("Sales: {} Customers: {}".format(
        output_sales[0], output_customers[0]))
