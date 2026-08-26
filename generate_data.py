import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_synthetic_data(num_samples=5000):
    print(f"Generating {num_samples} synthetic records...")
    
    # 10 Common Symptoms
    symptoms = [
        "Fever", "Headache", "Cough", "Fatigue", "Body Pain", 
        "Sore Throat", "Nausea", "Chills", "Runny Nose", "Shortness of Breath"
    ]
    
    # 8 Common Diseases
    diseases = [
        "Common Cold", "Flu", "COVID-19", "Dengue", 
        "Malaria", "Typhoid", "Gastroenteritis", "Migraine"
    ]
    
    data = []
    
    for _ in range(num_samples):
        # Generate target disease
        disease = random.choice(diseases)
        
        # Determine symptoms based on the disease (probabilistic)
        record = {}
        
        # Common Cold: Cough, Runny Nose, Sore Throat, Fatigue
        if disease == "Common Cold":
            probs = [0.1, 0.3, 0.8, 0.4, 0.1, 0.7, 0.0, 0.1, 0.9, 0.0]
        # Flu: Fever, Cough, Fatigue, Body Pain, Chills
        elif disease == "Flu":
            probs = [0.9, 0.6, 0.8, 0.9, 0.8, 0.4, 0.2, 0.7, 0.4, 0.1]
        # COVID-19: Fever, Cough, Fatigue, Shortness of Breath, Sore Throat
        elif disease == "COVID-19":
            probs = [0.8, 0.6, 0.8, 0.7, 0.5, 0.6, 0.1, 0.4, 0.3, 0.7]
        # Dengue: Fever, Headache, Body Pain, Nausea, Fatigue
        elif disease == "Dengue":
            probs = [0.9, 0.8, 0.1, 0.9, 0.9, 0.1, 0.7, 0.5, 0.1, 0.0]
        # Malaria: Fever, Chills, Headache, Fatigue, Nausea
        elif disease == "Malaria":
            probs = [0.9, 0.7, 0.2, 0.8, 0.6, 0.0, 0.6, 0.9, 0.0, 0.0]
        # Typhoid: Fever, Headache, Fatigue, Nausea, Body Pain
        elif disease == "Typhoid":
            probs = [0.9, 0.8, 0.1, 0.9, 0.6, 0.1, 0.7, 0.5, 0.0, 0.0]
        # Gastroenteritis: Nausea, Fatigue, Fever (mild), Body Pain (cramps)
        elif disease == "Gastroenteritis":
            probs = [0.4, 0.2, 0.0, 0.8, 0.7, 0.0, 0.9, 0.2, 0.0, 0.0]
        # Migraine: Headache, Nausea, Fatigue
        elif disease == "Migraine":
            probs = [0.0, 0.9, 0.0, 0.7, 0.2, 0.0, 0.6, 0.0, 0.0, 0.0]
        else:
            probs = [0.1] * len(symptoms)
        
        # Add some random noise
        for i, symptom in enumerate(symptoms):
            # 5% chance of random symptom appearing or not appearing despite the probabilities
            if random.random() < 0.05:
                record[symptom] = random.choice([0, 1])
            else:
                record[symptom] = np.random.choice([0, 1], p=[1-probs[i], probs[i]])
                
        record["Target_Disease"] = disease
        data.append(record)
        
    df = pd.DataFrame(data)
    
    # Ensure all columns are in order
    columns_order = symptoms + ["Target_Disease"]
    df = df[columns_order]
    
    return df

if __name__ == "__main__":
    output_file = "symptom_disease_dataset.csv"
    df = generate_synthetic_data(5000)
    df.to_csv(output_file, index=False)
    print(f"Successfully generated dataset and saved to '{output_file}'")
    print(df.head())
    print("\nDataset Shape:", df.shape)
    print("Class Distribution:\n", df['Target_Disease'].value_counts())
