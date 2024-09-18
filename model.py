from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest Classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the model
joblib.dump(clf, 'iris_model.pkl')

print("Model trained and saved!")
