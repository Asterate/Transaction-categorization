import pandas as pd

raw_data = pd.read_csv('../dataset/transaction_dataset.csv', delimiter=',')
print(raw_data.head())
#print(raw_data.tail())
#print(raw_data.isna())
#print(raw_data.info())
#print(raw_data.describe())