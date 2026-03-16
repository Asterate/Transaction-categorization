import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

raw_data = pd.read_csv('../dataset/transaction_dataset.csv', delimiter=',')
X = raw_data["transaction_description"]
Y = raw_data["category"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
X_test_original = X_test.copy()

vec = CountVectorizer()
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

model = MultinomialNB()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
for desc, pred, actual in zip(X_test_original, Y_pred, Y_test):
    print(f"Description : {desc}")
    print(f"Predicted   : {pred}")
    print(f"Actual      : {actual}")
    print("---")