import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from data_generation import generate_synthetic_credit_data

# Ensure data exists
try:
    df = pd.read_csv('credit_data.csv')
)
except FileNotFoundError:
    generate_synthetic_credit_data()
    df = pd.read_csv('credit_data.csv')

X = df.drop('default', axis=1)
y = df['default']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Training Random Forest Classifier on Credit Risk Data...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print("\n--- Model Evaluation Results ---")
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
