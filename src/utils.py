###############################################################################
# File:         utils.py
# Author:       Pierre Lasbleis
# Description:  Contains the functions to read the dataset.
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

Arguments: 
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




"""
Function loadTestData()
Produce a list of entries containing the test data. 

Arguments: 
* url_csv: a string containing the location of a csv file with one header line 
and the folowing fields:
    * Id: Integer
    * Store: Integer
    * DayOfWeek: Integer
    * Date: date
    * Open: Integer
    * Promo: Integer
    * StateHoliday: char
    * SchoolHoliday: char
    
Returns: 
    * data: a list. Each element is a list containing the fields as int 
    or char or datetime
"""
def loadTestData(url_csv):
    ################################
    # Local parser : on line field "open" missing on entry 480
    ################################
    def localIntParser(txt_str):
        if len(txt_str) > 0:
            return int(txt_str)
        else:
            return 0
    ############ end of local parser


    # Load file
    content = -1
    with open(url_csv, 'r') as fid:
        content = fid.read()
        
    if content == -1:   # empty file or reading problem    
        return []
    else:               # File read
        data = list()
    
        lines = content.split('\n')[1:-1] # Skip header and last (empty) line
        for l in lines:
            fields = l.split(',')
            
            # Read fields
            data.append([
                int(fields[1]),             # Store id
                int(fields[2]),             # Day of week
                date(
                    int(fields[3][:4]),     # Year 
                    int(fields[3][5:7]),    # Month
                    int(fields[3][8:10])),  # Day
                localIntParser(fields[4]),  # Open
                int(fields[5]),             # Promo
                fields[6][1],               # StateHoliday
                fields[7][1]                # SchoolHoliday
                ])
                
        return data




        
""" 
Function separateTrainingSet()
Seperate the training data into training set and test set using a uniform 
probability distribution.

Arguments: 
    * data: training data, as generated by the function loadTrainingData()
    * output_sales:     "
    * output_customers: "
    * pct_tr: pourcentage of entries in the training set. Must be in the 
    range [0;100]. 
    
Returns: 
    * data_tr: input entries for the training set
    * sales_tr: sales output for the training set
    * customer_tr: customer output for the training set
    * data_te: input entries for the test set
    * sales_te: sales output for the test set
    * customer_te: customer output for the test set
"""
def separateTrainingSet(data, output_sales, output_customers, pct_tr):
    N = len(data)
    indices = np.arange(N)
    np.random.shuffle(indices)
    
    indices_tr = indices[:int(N/100.*pct_tr)]   # training set
    indices_te = indices[int(N/100.*pct_tr):]   # test set
    
    return [data[i] for i in indices_tr],           \
        [output_sales[i] for i in indices_tr],      \
        [output_customers[i] for i in indices_tr],  \
        [data[i] for i in indices_te],              \
        [output_sales[i] for i in indices_te],      \
        [output_customers[i] for i in indices_te]

"""
Function compute_RMSPE()

Arguments: 
    * y: Numpy vector containing the true outputs
    * y_hat: Numpy vector containing the estimated outputs

Returns: 
    * RMSPE computed on the non-zero true outputs. 
"""
def compute_RMSPE(y, y_hat):
    ind = np.where(y!=0)[0]
    
    return np.sqrt( 
        np.sum( ((y[ind] - y_hat[ind])/y[ind]) ** 2 ) / 
        ind.shape[0]
        )
        
""" 
Main function to test the other functions. 
"""
if __name__ == "__main__":
    print(loadStoreInfo("../data/store.csv")[0])
    
    (input, output_sales, output_customers) = loadTrainingData("../data/train.csv")
    
    print(input[0])
    print("Sales: {} Customers: {}".format(
        output_sales[0], output_customers[0]))
        
    (i_tr, o_s_tr, o_c_tr, i_te, o_s_te, o_c_te) = separateTrainingSet(
        input, output_sales, output_customers, 80)
        
    print(i_tr[0])
    print("Sales: {} Customers: {}".format(
        o_s_tr[0], o_c_tr[0]))
        
    print("{} entries in training set ; {} entries in test set".format(
        len(i_tr), len(i_te)))

    print("If we predict zero sales everyday, RMSPE = {}".format(
        compute_RMSPE(
            np.array(o_s_te), np.zeros((np.array(o_s_te).shape[0])))))
