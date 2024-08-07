import requests
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configurer le logger
logging.basicConfig(level=logging.INFO)

# Remplacer 'YOUR_API_KEY' par votre clé API de Capital.com
API_KEY = '7r532CwX1fLHqEav'
BASE_URL = 'https://api-capital.backend-capital.com'

def place_order(instrument_id, order_type, quantity, direction):
    url = f"{BASE_URL}/api/v1/accounts/orders"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'instrumentId': instrument_id,
        'orderType': order_type,
        'quantity': quantity,
        'direction': direction
    }
    response = requests.post(url, json=data, headers=headers)
    logging.info(f"Order response: {response.json()}")  # Ajouter un message de log
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f"Webhook received: {data}")  # Ajouter un message de log

    # Identifiant de l'instrument pour le gold (à adapter selon le bon identifiant de Capital.com)
    instrument_id = "gold"
    
    # Type d'ordre, par exemple "market" pour un ordre au marché
    order_type = "market"
    
    # Lot de 0.1
    quantity = 0.1

    # Déterminer la direction de l'ordre (buy ou sell) en fonction des données reçues
    direction = data.get('direction', 'buy')  # Par défaut, acheter

    response = place_order(instrument_id, order_type, quantity, direction)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
