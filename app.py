#deploy_model = pkl.load(open('model_1.pkl', 'rb'))

# using flask to make an API
from flask import Flask, request, jsonify
import pickle as pkl
import os

app = Flask(__name__)


os.chdir('G:\My Drive\Prep\Prep\Linear Regression Proj 1')

model = pkl.load(open('model_1.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[data['TV']]])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)