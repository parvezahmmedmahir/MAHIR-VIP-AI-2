from flask import Flask, jsonify, request
from flask_cors import CORS
from quotex_api import api
from config import MARKET_PAIRS
import random

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Initialize API connection for serverless
api.connect()

@app.route('/')
def home():
    return jsonify({"status": "online", "system": "MAHIR VIP AUTO AI Backend"})

@app.route('/api/assets', methods=['GET'])
def get_assets():
    return jsonify({"assets": MARKET_PAIRS})

@app.route('/api/signal', methods=['POST', 'GET'])
def generate_signal():
    """
    Generates a signal for a random asset or a specific one if requested.
    """
    try:
        # Select a random asset from the configuration
        asset = random.choice(MARKET_PAIRS)
        
        # Analyze the market for this asset
        analysis = api.analyze_market(asset)
        
        response = {
            "success": True,
            "data": {
                "pair": analysis["asset"],
                "direction": analysis["signal"],
                "expiry": "1 MINUTE",
                "confidence": f"{analysis['confidence']}%",
                "strategy": analysis["strategy"],
                "timestamp": analysis["timestamp"]
            }
        }
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    print("Starting MAHIR VIP AUTO AI Server...")
    print("Initializing API connection...")
    app.run(host='0.0.0.0', port=5000, debug=True)
