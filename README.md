# RossmannSales
Repository containing my solution for the Rossmann Store Sales challenge 
from Kaggle.

Challenge description and data on https://www.kaggle.com/c/rossmann-store-sales. 

In order to use this code, you need the following tools:
 * Python 3.x (the code was tested on Python 3.5.2)
 * Jupyter Notebook
 * Numpy (Python library, version 1.12.0)
 * Scikit-learn (Python library, version 0.18.1)
 
Then you need the files containing the data (available on https://www.kaggle.com/c/rossmann-store-sales/data):
 * store.csv
 * test.csv
 * train.csv
 
To use the code:

1. Modify the file SETTINGS.json to indicate the path to the different csv 
   files, to the file in which the model will be saved and to the file that 
   will contain the submission.

2. Run the notebook src/train.ipynb to load the training data, train the 
   model and save the model. 

3. Run the notebook src/predict.ipynb to load the test data and the model
   and generate predictions.  The predictions will be saved in a csv file 
   using the path provided in SETTINGS.json.    