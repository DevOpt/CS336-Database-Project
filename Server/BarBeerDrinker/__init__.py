from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

from BarBeerDrinker import database

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/bar", methods=["GET"])
def get_bars():
    return jsonify(database.get_bars())

@app.route("/api/bar/<name>", methods=["GET"])
def find_bar(name):
    try:
        if name is None:
            raise ValueError("Bar is not specified.")
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with the given name.", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/beers_cheaper_than", methods=["POST"])
def find_beers_cheaper_than():
    body = json.loads(request.data)
    max_price = body['maxPrice']
    return jsonify(database.filter_beers(max_price))