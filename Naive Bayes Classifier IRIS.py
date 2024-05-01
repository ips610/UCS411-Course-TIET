import pandas as pd
import sklearn.preprocessing as sk
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import sklearn.metrics as m


data = pd.read_csv("./IRIS.csv")
print(data.head())
print(data.dtypes)
print(data.describe())

#sepal_length,sepal_width,petal_length,petal_width,species
features = sk.scale(
    data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
)

pd.DataFrame(features).describe()

target = data["species"]

print(target.value_counts())

target = pd.Series(sk.LabelEncoder().fit_transform(target))
print(target.value_counts())

x_train, x_test, y_train, y_test = ms.train_test_split(features, target, test_size=0.20)
print(len(x_train), len(x_test))
print(len(y_train), len(y_test))

bc = nb.GaussianNB()
bc.fit(x_train, y_train)
pred = bc.predict(x_test)

print("accuracy:", m.accuracy_score(pred, y_test))
print("precision (None):", m.precision_score(pred, y_test, average=None))
print("precision (micro):", m.precision_score(pred, y_test, average="micro"))
print("precision (macro):", m.precision_score(pred, y_test, average="macro"))
print("precision (weighted):", m.precision_score(pred, y_test, average="weighted"))
print("recall:", m.recall_score(pred, y_test, average="micro"))
print("f1_score:", m.f1_score(pred, y_test, average="micro"))

print(m.classification_report(pred, y_test))