from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook/<endpoint>', methods=['POST'])
def dynamic_webhook(endpoint):
    print("Starting Now")
    print("Headers:", request.headers)  # Print request headers
    print("Raw Data:", request.data)    # Print raw payload
    
    # Safely attempt to parse JSON
    try:
        data = request.get_json()
        if data is None:
            raise ValueError("No JSON in request")
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return jsonify({"Abingus": "Adingus"})

    print(f"Received data for {endpoint}: {data}")
    return jsonify({"status": "success", "endpoint": endpoint, "received": data}), 200

if __name__ == '__main__':
    print("About to start")
    # Use the PORT environment variable if available, default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
