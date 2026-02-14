# Anne Tran (UCID: 30286177)
# Assign3_Q4

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("kidney_disease.csv")

df = df.dropna() # remove missing rows in dataset

# create the feature matrix excluding the "classification" column
feature_matrix=pd.get_dummies(df.drop(columns=["classification"]))

# create the vector y
classification=df["classification"]


# Obtain the train & test data
feature_train, feature_test, classification_train, classification_test=train_test_split(
    feature_matrix, classification,
    test_size=0.30,
    random_state=0
)

knn_model=KNeighborsClassifier(n_neighbors=5) # define the model
trained_knn_model=knn_model.fit(feature_train, classification_train) #train model

classification_predict=trained_knn_model.predict(feature_test)
confusion_matrix=confusion_matrix(classification_test, classification_predict)

accuracy=accuracy_score(classification_test, classification_predict)
precision=precision_score(classification_test, classification_predict, pos_label='ckd')
recall=recall_score(classification_test, classification_predict, pos_label='ckd')
f1Score=f1_score(classification_test, classification_predict, pos_label='ckd')

# Display the result
print(f"Confusion matrix: \n {confusion_matrix}")
print(f"Accuracy: {accuracy:0.3f}")
print(f"Precision: {precision}")
print(f"Recall: {recall:0.3f}")
print(f"F1 score: {f1Score:0.3f}")

# Answer the questions------------------------------------------------------------------------
# True Positive: model predict kidney disease in patient has kidney disease
# True Negative: model predict there is no kidney disease in patient actually has no kidney disease
# False Positive : model predict kidney disease in patient actually have no kidney disease
# False Negative: model predict no kidney disease in patient has kidney disease

# Accuracy shows the percentage of correct prediction, however bad model can have high accuracy as well since it cannot handle or miss kidney patient.
# Recall is the most important metric because it detect of true response which is actual kidney disease patient so it can shows more precisely about the accuracy of this model.
