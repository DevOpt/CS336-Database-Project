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

@app.route("/api/menu/<name>", methods=["GET"])
def get_menu(name):
    try:
        if name is None:
            raise ValueError('Bar is not specified')
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with the given name,",404)
        return jsonify(database.get_bar_menu(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/bar-cities", methods=["GET"])
def get_bar_cities():
    try:
        return jsonify(database.get_bar_cities())
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/beer", methods=["GET"])
def get_beers():
    try:
        return jsonify(database.get_beers())
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/beer-name", methods=["GET"])
def get_beers_name():
    try:
        return jsonify(database.get_beers_name())
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/beer-manufacturer", methods=["GET"])
def get_beer_manufacturers():
    try:
        return jsonify(database.get_beer_manufacturers(None))
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/beer-manufacturer/<beer>", methods=["GET"])
def get_manufacturers_making(beer):
    try:
        return jsonify(database.get_beer_manufacturers(beer))
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/likes", methods=["GET"])
def get_likes():
    try:
        drinker = request.args.get("drinker")
        if drinker is None:
            raise ValueError("Drinker is not specified")
        return jsonify(database.get_likes(drinker))
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/drinker", methods=["GET"])
def get_drinkers():
    try:
        return jsonify(database.get_drinkers())
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/drinker/<name>", methods=["GET"])
def get_drinker(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified")
        return jsonify(database.get_drinker_info(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/drinker/most-ordered/<name>", methods=["GET"])
def get_most_ordered_beer(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified")
        return jsonify(database.get_most_ordered_beer(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/drinker-transactions/<name>", methods=["GET"])
def get_drinker_transactions(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified")
        return jsonify(database.get_drinker_transactions(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/bars-selling/<beer>", methods=["GET"])
def find_bars_selling(beer):
    try:
        if beer is None:
            raise ValueError("Beer is not specified")
        return jsonify(database.get_bars_selling(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/frequents-data", methods=["GET"])
def get_bar_frequent_counts():
    try:
        return jsonify(database.get_bar_frequent_counts())
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-spenders/<name>", methods=["GET"])
def get_top_spenders(name):
    try:
        if name is None:
            raise ValueError('Bar is not specified')
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with the given name,",404)
        return jsonify(database.get_top_spenders(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-beers/<name>", methods=["GET"])
def get_top_beers(name):
    try:
        if name is None:
            raise ValueError('Bar is not specified')
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with the given name,",404)
        return jsonify(database.get_top_beers(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/transactions/<name>", methods=["GET"])
def num_of_transactions(name):
    try:
        if name is None:
            raise ValueError('Bar is not specified')
        bar = database.find_bar(name)
        if bar is None:
            return make_response("No bar found with the given name,",404)
        return jsonify(database.num_of_transactions(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/inventory/fraction/<name>/<day>", methods=["GET"])
def get_bar_inventory(name, day):
    try:
        return jsonify(database.get_bar_inventory(name, day))
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-bars/<beer>/<day>", methods=["GET"])
def get_top_bars(beer, day):
    try:
        if beer is None:
            raise ValueError("Beer or day is not specified")
        return jsonify(database.get_top_bars(beer, day))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-bars/<beer>", methods=["GET"])
def get_top_bars_for(beer):
    try:
        if beer is None:
            raise ValueError("Beer is not specified")
        return jsonify(database.get_top_bars(beer, None))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-drinkers/<beer>", methods=["GET"])
def get_top_drinkers(beer):
    try:
        if beer is None:
            raise ValueError("Beer is not specified")
        return jsonify(database.get_top_drinkers(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/popular-times/<bar>", methods=["GET"])
def popular_times(bar):
    try:
        if bar is None:
            raise ValueError("Bar is not specified")
        return jsonify(database.popular_times(bar))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/top-manf-sales/<manf>", methods=["GET"])
def get_top_manf_sales(manf):
    try:
        if manf is None:
            raise ValueError("Maunfacturer is not specified")
        return jsonify(database.get_top_manf_sales(manf))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/cities-like-manf/<manf>", methods=["GET"])
def get_cities_like_manf(manf):
    try:
        if manf is None:
            raise ValueError("Maunfacturer is not specified")
        return jsonify(database.get_cities_like_manf(manf))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

