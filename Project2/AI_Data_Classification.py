from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create AI Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

# Make Predictions
predictions = model.predict(X_test)

# Check Accuracy
accuracy = accuracy_score(y_test, predictions)

print("===== AI DATA CLASSIFICATION PROJECT =====")
print("Dataset: Iris")
print("Algorithm: Decision Tree Classifier")
print("Accuracy:", accuracy)
