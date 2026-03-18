from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World! 🌍"

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from DevOps project!"})

@app.route('/status')
def status():
    return jsonify({"status": "running", "port": 5000})

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
