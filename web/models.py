from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

import joblib 

data = load_iris()

x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = AdaBoostClassifier()
model.fit(x_train, y_train)

joblib.dump(model, 'model.dmp')