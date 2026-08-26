# pyrefly: ignore [missing-import]
import joblib
import pandas as pd
import os
import sys

def predict_disease():
    model_filename = "disease_prediction_model.pkl"
    features_filename = "feature_names.pkl"
    
    if not os.path.exists(model_filename) or not os.path.exists(features_filename):
        print("Error: Trained model not found. Please run train_model.py first.")
        return
        
    print("Loading trained model...")
    model = joblib.load(model_filename)
    features = joblib.load(features_filename)
    
    print("\n" + "*"*50)
    print("      AI-BASED DISEASE PREDICTION SYSTEM      ")
    print("*"*50)
    print("Please answer the following questions with 'yes' or 'no'.\n")
    
    user_input = {}
    
    for symptom in features:
        while True:
            # sys.stdout.write ensures prompt works cleanly with testing scripts
            sys.stdout.write(f"Do you have {symptom}? (yes/no): ")
            sys.stdout.flush()
            ans = sys.stdin.readline().strip().lower()
            if ans in ['yes', 'y']:
                user_input[symptom] = 1
                break
            elif ans in ['no', 'n']:
                user_input[symptom] = 0
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                
    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])
    
    # Predict
    print("\nAnalyzing symptoms...")
    prediction = model.predict(input_df)[0]
    
    print("\n" + "="*50)
    print(f"              PREDICTION RESULT               ")
    print("="*50)
    print(f"Based on the symptoms provided, you might have:")
    print(f"                >> {prediction.upper()} <<")
    print("="*50)
    print("Disclaimer: This is a synthetic prediction system and not medical advice.")
    print("Please consult a doctor for a professional medical diagnosis.")
    
if __name__ == "__main__":
    try:
        predict_disease()
    except KeyboardInterrupt:
        print("\nExiting system.")
