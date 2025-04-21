from flask import Flask, request, jsonify
from selenium_script import get_customer_id

app = Flask(__name__)


# Basic GET route for browser testing
@app.route('/', methods=['GET'])
def home():
    return "Flask app is running!"


# Your original POST route
@app.route('/get_customer_id', methods=['POST'])
def get_customer():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    acc_no = data.get("account_number")

    if not acc_no:
        return jsonify({"error": "No account number provided"}), 400

    try:
        customer_id = get_customer_id(acc_no)
        return jsonify({"customer_id": customer_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
