import numpy as np
import pickle
from flask import Flask , request ,render_template

app = Flask(__name__)

model1 = pickle.load(open('Model/Regression.pkl','rb'))
model2 = pickle.load(open('Model/NeuralNetwork.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature_names = request.form.keys()
    intFeatures = [float(request.form.get(name)) for name in feature_names]
    Features = np.array([intFeatures])
    # intFeatures = [float(x) for x in request.form.values]
    # Features = [np.arry(intFeatures)]
    predictionValue1 = model1.predict(Features)
    predictionValue2 = model2.predict(Features)

    return render_template('index.html',predictionText='The predicted strength of concrete using regression is {}  and using Nerural network is {}'.format(predictionValue1,predictionValue2))
if __name__ == "__main__":
    app.run()

# import numpy as np
# import pickle
# from flask import Flask, request, render_template

# app = Flask(__name__)

# # Load models with error handling
# try:
#     model1 = pickle.load(open('Model/Regression.pkl', 'rb'))
#     model2 = pickle.load(open('Model/NeuralNetwork.pkl', 'rb'))
# except Exception as e:
#     print(f"Error loading models: {e}")

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Debug print statements
#         print("Received request with form data:", request.form)

#         # Extract features from form
#         feature_names = request.form.getlist('feature_names')  # Ensure 'feature_names' matches form input names
#         print("Feature names:", feature_names)

#         intFeatures = [float(request.form.get(name, 0)) for name in feature_names]
#         print("Features converted to float:", intFeatures)

#         # Prepare feature array for prediction
#         Features = [np.array(intFeatures)]

#         # Debug print statements
#         print("Features array for prediction:", Features)

#         # Predict using both models
#         predictionValue1 = model1.predict(Features)
#         predictionValue2 = model2.predict(Features)

#         # Return result to the template
#         result = f'The predicted strength of concrete using regression is {predictionValue1[0]} and using Neural network is {predictionValue2[0]}'
#         print("Prediction result:", result)

#         return render_template('index.html', predictionText=result)

#     except Exception as e:
#         # Log error details
#         print(f"Error during prediction: {e}")
#         return render_template('index.html', predictionText='An error occurred during prediction.')

# if __name__ == "__main__":
#     app.run(debug=True)  # Enable debug mode for better error messages
  # Enable debug mode for better error messages
