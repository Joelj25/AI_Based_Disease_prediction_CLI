import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
# pyrefly: ignore [missing-import]
import joblib
import os

def train_and_evaluate():
    data_file = "symptom_disease_dataset.csv"
    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found. Please run generate_data.py first.")
        return
        
    print(f"Loading data from {data_file}...")
    df = pd.read_csv(data_file)
    
    # Preprocessing
    print("Preprocessing data...")
    X = df.drop("Target_Disease", axis=1)
    y = df["Target_Disease"]
    
    # Train-test split
    print("Splitting dataset into training and testing sets (80-20)...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model Training
    print("Initializing Decision Tree Classifier...")
    model = DecisionTreeClassifier(random_state=42, max_depth=10)
    
    print("Training the model...")
    model.fit(X_train, y_train)
    
    # Model Evaluation
    print("Evaluating the model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print("\n" + "="*40)
    print(f"Model Training Complete!")
    print(f"Accuracy Score: {accuracy * 100:.2f}%")
    print("="*40 + "\n")
    
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the trained model and feature names
    model_filename = "disease_prediction_model.pkl"
    features_filename = "feature_names.pkl"
    
    print(f"Saving model logic to {model_filename}...")
    joblib.dump(model, model_filename)
    joblib.dump(list(X.columns), features_filename)
    
    print("Model saved successfully.")

if __name__ == "__main__":
    train_and_evaluate()
