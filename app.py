import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api-capital.backend-capital.com'

def place_order(instrument_id, order_type, quantity):
    url = f"{BASE_URL}/api/v1/accounts/orders"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'instrumentId': instrument_id,
        'orderType': order_type,
        'quantity': quantity,
        'direction': 'buy' if order_type == 'market' else 'sell'
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    instrument_id = data.get('instrument_id')
    order_type = data.get('order_type')
    quantity = data.get('quantity')
    response = place_order(instrument_id, order_type, quantity)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
