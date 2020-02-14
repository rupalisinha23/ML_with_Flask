import pickle
from flask import Flask, request
import numpy as np
import pandas as pd

# load the pickle file
with open('./model/rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict')
def predict_iris():
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    prediction = model.predict(np.array([[s_length, s_width, \
                                    p_length, p_width]]))

    return str(prediction)


@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))


if __name__ == '__main__':
    app.run()