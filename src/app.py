from flask import Flask, request, jsonify
import hashlib
from blockchain import register_content, get_content_owner

app = Flask(__name__)

def hash_content(content):
    return hashlib.sha256(content).hexdigest()

@app.route('/register', methods=['POST'])
def register():
    file = request.files['file']
    content_hash = hash_content(file.read().encode())
    
    tx_hash = register_content(content_hash)
    return jsonify({"message": "Content registered", "transaction": tx_hash})

@app.route('/owner/<content_hash>', methods=['GET'])
def get_owner(content_hash):
    owner, timestamp = get_content_owner(content_hash)
    return jsonify({"owner": owner, "timestamp": timestamp})

if __name__ == '__main__':
    app.run(debug=True)
