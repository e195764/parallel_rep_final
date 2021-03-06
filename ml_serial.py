# import the library
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score # 正解率(accuracy)
from sklearn.metrics import f1_score # F値
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# load the dataset
dataset_org = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Convert to the matrix
dataset = dataset_org.to_numpy()
np.set_printoptions(suppress=True, precision=2)

# Create the new matrix without test-data
X = dataset[:,0:12]

# standardize X
sc = StandardScaler()
X_std = sc.fit_transform(X)

# Create the test-data
y = dataset[:,12]

# Split the dataset into training and testing set(sklearn)
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size = 0.5)


# Create linearSVC object
lin_clf = svm.LinearSVC()

# Train the model using the training set
lin_clf.fit(X_train, y_train)

# Make predictions using the testing set
predicted = lin_clf.predict(X_test)

# 正解率(accuracy), Accuracy = (TP + TN) / (TP + TN + FP + FN)
print("LinearSVCの正解率 = " + '{:.2f}'.format(accuracy_score(y_test, predicted)))

# F値, F1 = 2 * (precision * recall) / (precision + recall)
print("LinearSVCのF値 = " + '{:.2f}'.format(f1_score(y_test, predicted)))

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_train)
predicted = knn_clf.predict(X_test)
print("KNNの正解率 = " + '{:.2f}'.format(accuracy_score(y_test, predicted)))
print("KNNのF値 = " + '{:.2f}'.format(f1_score(y_test, predicted)))

clf = svm.SVC()
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
print("SVCの正解率 = " + '{:.2f}'.format(accuracy_score(y_test, predicted)))
print("SVCのF値 = " + '{:.2f}'.format(f1_score(y_test, predicted)))
