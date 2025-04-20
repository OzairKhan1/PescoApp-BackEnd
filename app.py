# app.py (Flask backend)
from flask import Flask, request, jsonify
from selenium_script import get_customer_id

app = Flask(__name__)

@app.route('/get_customer_id', methods=['POST'])
def get_customer():
    data = request.get_json()
    acc_no = data.get("account_number")

    if not acc_no:
        return jsonify({"error": "No account number provided"}), 400

    customer_id = get_customer_id(acc_no)
    return jsonify({"customer_id": customer_id})

if __name__ == '__main__':
    app.run(debug=True)
