from flask import Flask, jsonify, request
from model_files.model import predict
import numpy as np
app = Flask("model_prediction")


@app.route('/', methods=['POST'])
def predict_result():
    images = request.json
    l = images['left_eye']
    r = images['right_eye']
    l_eye = np.array(l)
    r_eye = np.array(r)
    flag = predict(l_eye, r_eye)
    result = {
        'isclosed': flag
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run()
