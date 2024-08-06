import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/custom_static')

# Load models with error handling
try:
    model1 = pickle.load(open('Model/Regression.pkl', 'rb'))
    model2 = pickle.load(open('Model/NeuralNetwork.pkl', 'rb'))
except Exception as e:
    print(f"Error loading models: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
    # Debug print statements
        print("Received request with form data:", request.form)

        # Extract features from form
        feature_names = request.form.keys()
        intFeatures = [float(request.form.get(name)) for name in feature_names]
        Features = np.array([intFeatures])

        # Debug print statements
        print("Features array for prediction:", Features)

        # Predict using both models
        predictionValue1 = model1.predict(Features)
        predictionValue2 = model2.predict(Features)

        # Return result to the template
        result = f'The predicted strength of concrete using regression is {round(predictionValue1[0],2)} and using Neural network is {round(predictionValue2[0][0],2)}'
        print("Prediction result:", result)

        return render_template('index.html', predictionText=result)

    except Exception as e:
        # Log error details
        print(f"Error during prediction: {e}")
        return render_template('index.html', predictionText='An error occurred during prediction.')

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error messages
