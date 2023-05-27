from flask import Flask, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)

# Load the trained model
model = None

@app.before_first_request
def load_model():
    global model
    model = pickle.load(open('loan_prediction.pkl', 'rb'))


def preprocess_data(data):
    df = pd.DataFrame(data, index=[0])  # Provide index as a list containing a single element
    return df

    # Select the required features
    selected_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome',
                         'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']

    # Extract the selected features from the DataFrame
    input_data = df[selected_features]

    return input_data

# Define a route for your API
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Preprocess the input data
    input_data = preprocess_data(data)

    # Make predictions using the loaded model
    predictions = model.predict(input_data)

    # Prepare the response as JSON
    response = {
        'predictions': predictions.tolist()
    }

    return jsonify(response)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)