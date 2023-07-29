# service2.py
import requests
from flask import Flask, request

app = Flask(__name__)

SERVICE1_URL = 'http://service1:8000/calculate_hash'

def calculate_webpage_hash(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = {'text': response.text}
        response = requests.post(SERVICE1_URL, json=data)
        if response.status_code == 200:
            return response.json()['hash']
    return None

@app.route('/hash_webpage', methods=['POST'])
def hash_webpage():
    data = request.get_json()
    if 'url' not in data:
        return "Error: 'url' parameter not provided.", 400

    url = data['url']
    hash_value = calculate_webpage_hash(url)
    if hash_value:
        return {'hash': hash_value}
    else:
        return "Error: Unable to calculate hash for the webpage.", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
