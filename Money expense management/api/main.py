from flask import Flask
from flask import jsonify

#Guardando el servidos flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to tomorrowland'

@app.route('/api/v1/transactions', methods=['GET'])
def get_transactions():
    response = {'name': 'c'}
    return jsonify(response)

@app.route('/api/v1/transactions', methods=['POST'])
def save_transactions():
    response = 'melo'
    return jsonify(response)

@app.route('/api/v1/transactions', methods=['DELETE'])
def delete_transactions():
    response = ':c'
    return jsonify(response)

if (__name__ == '__main__'):
    app.run(debug=False)