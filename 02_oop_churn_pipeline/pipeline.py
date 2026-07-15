import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class DataPipeline:
    """Handles professional modular data engineering steps."""
    def __init__(self, test_size=0.2):
        self.test_size = test_size
        
    def create_mock_data(self):
        np.random.seed(24)
        data = np.random.rand(500, 4)
        labels = np.random.choice([0, 1], size=500, p=[0.7, 0.3])
        df = pd.DataFrame(data, columns=['tenure', 'monthly_charges', 'usage_frequency', 'support_calls'])
        df['churn'] = labels
        return df

    def execute(self):
        df = self.create_mock_data()
        X = df.drop('churn', axis=1)
        y = df['churn']
        return train_test_split(X, y, test_size=self.test_size, random_state=42)

class MLModelSystem:
    """Encapsulates model training mechanics utilizing clean architecture abstractions."""
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        
    def evaluate(self, X_test, y_test):
        accuracy = self.model.score(X_test, y_test)
        return {"Accuracy": accuracy}
