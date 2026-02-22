# Transaction-categorization

## Repository structure

```bash
├── dataset
│   ├── datasetLoad.py
│   │
│   ├── transaction_dataset.csv
│   
└── .gitignore
```

## Dataset
I chose a dataset from hugging face website. Found one that is meant for transaction categorizations.
I have included code to install the dataset yourself.

Requirements to download it with datasetLoad.py
- install Pandas
- install pyarrow
- install fastparquet
- huggingface_hub
- Hugging face account and read token
  -  hf auth login

Otherwise, the dataset is also available in transaction_dataset.csv 
