from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
data = [
{"id": 1, "name": "mahesh"},
{"id": 2, "name": "aruna"},
{"id": 3, "name": "mani"},
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
