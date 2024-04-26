# what will happen to variance if we use decison tree and your model is overfitting?
# what will happen to variance if we use decison tree and your model is underfitting?

# decision tree

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the iris dataset
data = load_iris()
X = data.data  # the features
y = data.target  # the target variable (labels)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80% training and 20% test

# Initialize the DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)

# Train Decision Tree Classifier
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Plotting the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=data.feature_names, class_names=data.target_names)
plt.title('Decision Tree of the Iris Dataset')
plt.show()