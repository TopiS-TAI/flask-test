import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def getFoliData():
    r = requests.get('http://data.foli.fi/siri/sm/20')
    data = r.json()
    return jsonify(data)

if (__name__ == '__main__'):
    app.run()