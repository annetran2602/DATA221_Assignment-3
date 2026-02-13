# Anne Tran (UCID: 30286177)
# Assign 2_Q3

import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("kidney_disease.csv")


# create matrix x contains all columns except 'classification'
feature_matrix=df.drop(columns=["classification"])

# Create a vector y using the 'classification'
classification=df.loc[:,["classification"]] # or y=df["classification"]

# split the dataset into training and testing
feature_train, classification_train, feature_test, classification_test=train_test_split(
    feature_matrix, classification, test_size=0.30, random_state=42)

