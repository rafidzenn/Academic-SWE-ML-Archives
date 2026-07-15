from pipeline import DataPipeline, MLModelSystem

def main():
    print("Initializing production-style OOP ML Pipeline...")
    pipeline = DataPipeline()
    X_train, X_test, y_train, y_test = pipeline.execute()

    model_system = MLModelSystem()
    model_system.train(X_train, y_train)
    metrics = model_system.evaluate(X_test, y_test)
    
    print("\nPipeline execution complete.")
    print(f"Metrics: {metrics}")

if __name__ == "__main__":
    main()
