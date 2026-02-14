# Anne Tran (UCID: 30286177)
# Assign3_Q5

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset into the dataframe
df=pd.read_csv("kidney_disease.csv", na_values="?")

df = df.dropna() # remove missing rows in dataset

# create the feature matrix excluding the "classification" column
feature_matrix=pd.get_dummies(df.drop(columns=["classification"]))

# create the vector y
classification=df["classification"]


# Obtain the train & test data
feature_train, feature_test, classification_train, classification_test=train_test_split(
    feature_matrix, classification,
    test_size=0.30,
    random_state=42
)

accuracyDict={}
kValues=[1,3,5,7,9]
for k in kValues:
    knn_model=KNeighborsClassifier(n_neighbors=k) # define the model
    trained_knn_model=knn_model.fit(feature_train, classification_train) # trained model
    classification_predict=trained_knn_model.predict(feature_test)
    accuracy=accuracy_score(classification_test, classification_predict)
    accuracyDict[k]=accuracy

# Sort the dict from high to low accuracy
sortedAccuracy={k:accuracyValue for k, accuracyValue in sorted(accuracyDict.items(), key=lambda item:item[1], reverse=True)}

# create a table
accuracyTable=pd.DataFrame({
    "k": list(sortedAccuracy.keys()),
    "Test Accuracy": list(sortedAccuracy.values())
})

print(f"Test accuracy corresponding with k values: \n {accuracyTable}")

# Print the k value has the highest accuracy and its accuracy
kList=[]
maxAccuracy=max(sortedAccuracy.values())
for k, accValue in sortedAccuracy.items():
    if accValue==maxAccuracy:
        kList.append(k)
print(f"The value of k: {kList} that has the highest accuracy is {maxAccuracy}")

# Answer the questions------------------------------------------------------------------------------------------
# Increasing k affects model's prediction and complexity by making model smoother and less sensitive to individual data points.
# Large k may cause underfitting because the model becomes simple and miss the unseen patterns
# Small k may cause overfitting because the model becomes complicated and sensitive with data.