import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

data = {
    "age": [25, 45, 52, 30, 60, 65, 40, 55, 35, 70],
    "blood_pressure": [120, 140, 150, 125, 160, 170, 130, 155, 120, 180],
    "cholesterol": [180, 240, 260, 190, 280, 300, 210, 270, 185, 310],
    "heart_disease": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["age", "blood_pressure", "cholesterol"]]

y = df["heart_disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")