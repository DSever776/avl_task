# service1.py
from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/calculate_hash', methods=['POST'])
def calculate_hash():
    data = request.get_json()
    if 'text' not in data:
        return "Error: 'text' parameter not provided.", 400

    text = data['text']
    hash_value = hashlib.sha256(text.encode()).hexdigest()
    return {'hash': hash_value}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
