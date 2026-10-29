from flask import Flask, request, jsonify
from calc import do_math

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        operation = request.form.get('Operation')
        data_a = request.form.get('Data_A')
        data_b = request.form.get('Data_B')

        if not operation or not data_a or not data_b:
            return jsonify({"error": "参数不全"}), 400

        a = float(data_a)
        b = float(data_b)
        result = do_math(operation, a, b)

        return jsonify({"Result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)