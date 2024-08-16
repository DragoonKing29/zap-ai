from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

model = joblib.load("models/ai_model.pkl")

def update_ai_model(new_data):
    X_new, y_new = np.array(new_data['features']), np.array(new_data['labels'])
    model.fit(X_new, y_new)
    joblib.dump(model, "models/ai_model.pkl")
    return {"status": "Model updated successfully"}
