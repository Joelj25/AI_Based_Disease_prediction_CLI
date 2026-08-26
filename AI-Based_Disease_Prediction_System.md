# AI-Based Disease Prediction System

## Project Title
AI-Based Disease Prediction System using Machine Learning

## Problem Statement
In today's fast-paced world, timely and accurate diagnosis of diseases based on symptoms is crucial. Misdiagnosis or delayed diagnosis can lead to severe health complications. There is a need for a reliable, automated system that can analyze common symptoms and provide an early indication of potential diseases.

## Objective
The primary objective of this project is to develop an end-to-end Machine Learning solution capable of predicting common diseases based on user-provided symptoms. The system aims to provide a simple Command-Line Interface (CLI) for users to check their symptoms and receive a quick, synthetic diagnosis, serving as an early-warning system.

## Tools & Technologies
- **Programming Language:** Python 3
- **Data Manipulation:** pandas, numpy
- **Machine Learning:** scikit-learn (Decision Tree Classifier)
- **Model Serialization:** joblib
- **Image Processing (for screenshots):** Pillow

## System Architecture / Model Description
The system architecture consists of three main modules:
1. **Data Generation & Preprocessing:** A synthetic dataset of 5,000 records mapping symptoms to diseases is generated. The preprocessing phase involves separating features (symptoms) from the target (disease) and splitting the data into training and testing sets.
2. **Model Training & Evaluation:** A Decision Tree Classifier is trained on the preprocessed dataset. The model's logic is then serialized and saved to disk.
3. **Interactive CLI Predictor:** A user-facing application that loads the trained model, collects symptom data interactively from the user, formats it, and outputs the predicted disease.

## Data Preprocessing and Algorithm Choice
**Data Preprocessing:**
- The data is generated as a structured pandas DataFrame.
- We separate the dataset into features (`X`) containing binary symptom values and labels (`y`) containing the target disease.
- We use an 80-20 train-test split (`train_test_split`) to ensure we have a robust testing set to validate the model's accuracy on unseen data.

**Algorithm Choice: Decision Tree Classifier**
We chose the Decision Tree Classifier for this specific problem because:
1. **Interpretability:** Decision trees mimic human decision-making processes, which is highly relevant in medical diagnosis (e.g., "If Fever = Yes AND Cough = Yes, then Flu").
2. **Handling Non-linear Data:** Symptoms often have complex, non-linear relationships with diseases. Decision trees naturally capture these non-linear interactions.
3. **No Feature Scaling Required:** Since our symptom features are binary (1 or 0), Decision Trees do not require normalization or scaling, streamlining the preprocessing pipeline.

## Code Explanation
- **`generate_data.py`:** Uses randomized probabilities to generate a synthetic but highly realistic dataset containing 10 symptoms and 8 target diseases.
- **`train_model.py`:** Reads the generated CSV, performs the train-test split, trains the `DecisionTreeClassifier`, prints the evaluation metrics, and saves `disease_prediction_model.pkl` and `feature_names.pkl`.
- **`disease_predictor.py`:** The CLI application. It prompts the user iteratively for symptom status, maps the input to a Pandas DataFrame matching the training feature structure, and uses `model.predict()` to display the final result.

## Results
- The Decision Tree classifier achieved an **Accuracy Score of 61.60%** on the synthetic test dataset.
- Considering the probabilistic nature and intentional random noise (5%) added to the 5,000 synthetic records to mimic real-world ambiguity, this score indicates the model has successfully learned the fundamental symptom-disease patterns.
- The interactive CLI provides a robust and seamless prediction experience.

## Conclusion
The AI-Based Disease Prediction System demonstrates how basic machine learning techniques can be applied to medical informatics. By structuring symptom data and applying a Decision Tree model, we successfully built a pipeline that processes symptoms and accurately infers potential illnesses.

## Future Scope
- **Integration with Real Data:** Replacing the synthetic dataset with real clinical datasets (like from Kaggle or WHO) to improve clinical accuracy.
- **Web Interface:** Upgrading the CLI to a modern web application (using Flask or Streamlit) or a mobile app for better accessibility.
- **Advanced Algorithms:** Implementing Random Forest or Neural Networks to capture more complex symptom intersections and boost accuracy.
- **Severity Analysis:** Adding features to analyze the severity or duration of symptoms for more granular predictions.
