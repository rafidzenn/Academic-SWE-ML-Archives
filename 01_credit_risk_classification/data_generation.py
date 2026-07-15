import numpy as np
import pandas as pd

def generate_synthetic_credit_data(num_samples=1000):
    np.random.seed(42)
    income = np.random.normal(50000, 15000, num_samples)
    debt = np.random.normal(20000, 10000, num_samples)
    credit_score = np.random.randint(300, 850, num_samples)
    
    # Calculate a simple deterministic probability for default risk
    risk_score = (debt / (income + 1)) * 5 - (credit_score / 850.0)
    default = (risk_score > np.median(risk_score)).astype(int)
    
    df = pd.DataFrame({
        'income': income,
        'debt': debt,
        'credit_score': credit_score,
        'default': default
    })
    df.to_csv('credit_data.csv', index=False)
    print("Synthetic credit data generated successfully.")

if __name__ == "__main__":
    generate_synthetic_credit_data()
