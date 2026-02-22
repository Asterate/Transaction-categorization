import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
df = pd.read_parquet("hf://datasets/mitulshah/transaction-categorization/default/train/0000.parquet")
df.to_csv('transaction_dataset.csv', index=False)