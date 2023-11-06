import pandas as pd
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv', delimiter=',')
df = df[~df.isnull().any(axis=1)]
df.PClass.unique()
df.PClass = df.PClass.map({'1st': 1, '2nd': 2, '3rd': 3}).astype(int)
df = df.drop(['PassengerID', 'Name', 'Sex'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(df.drop('Survived', axis=1), df.Survived, test_size=0.4)
model = svm.SVC()
model.fit(X_train, y_train)
y_pred_svc = model.predict(X_test)
acc_svc = round(model.score(X_train, y_train) * 100, 2)

model.predict(X_test[:10])
print(y_test[:10])
