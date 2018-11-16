from sqlalchemy import create_engine
from sqlalchemy import sql

from BarBeerDrinker import config

engine = create_engine(config.database_uri)

def get_bars():
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM BBDext.Bars;")
        return [dict(row) for row in rs]

def find_bar(name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM BBDext.Bars WHERE name = :name;"
        )

        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def filter_beers(max_price):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM BBDext.Sells WHERE price < :max_price;"
        )

        rs = con.execute(query, max_price = max_price)
        results = [dict(row) for row in rs]
        for r in results:
            r['price'] = float(r['price'])
        return results

def get_bar_menu(bar_name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT a.bar, a.beer, a.price, b.manf \
             FROM BBDext.Sells a \
             JOIN BBDext.Beer b \
             ON a.beer = b.name \
             WHERE a.bar = " + "\"" +bar_name +"\"" + ";"
        )

        rs = con.execute(query, name=bar_name)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['price'] = float(result[i]['price'])
        return result

def get_bars_selling(beer):
    with engine.connect() as con:
        query = sql.text(
            "SELECT a.bar, a.price \
             FROM BBDext.Sells a \
			 WHERE a.beer = " + "\"" + beer +"\"" + ";" 
        )
        rs = con.execute(query, beer = beer)
        results = [dict(row) for row in rs]
        for i, _ in enumerate(results):
            results[i]['price'] = float(results[i]['price'])
    return results

def get_bar_frequent_counts():
    return

def get_bar_cities():
    return

def get_beers():
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM BBDext.Beer;")
        return [dict(row) for row in rs]

def get_beer_manufacturers(beer):
    with engine.connect() as con:
        if beer is None:
            rs = con.execute('SELECT DISTINCT manf FROM BBDext.Beer')
            return [row['manf'] for row in rs]

        query = sql.text('SELECT manf FROM BBDext.Beer WHERE name = ' + '\"' + beer +'\"' + ';')
        rs = con.execute(query, beer=beer)
        result = rs.first()
        if result is None:
            return None
    return result['manf']

def get_drinkers():
    return

def get_likes(drinker_name):
    return

def get_drinker_info(drinker_name):
    return

# Given a beer, show top 10 bars where this beer sells the most, 
# show also drinkers who are the biggest consumers of this beer 
# as well as time distribution of when this beer sells the most.  
def get_most_selling(beer):
    return

# Include the bar they work at
def get_bartenders():
    return

# Given a bartender for a given bar, show all shifts of this bartender 
# in the past and how many beers of each brand did he/she sell.
def get_bartender(name):
    return

def get_top_spenders(bar_name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT drinker, total \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" +bar_name +"\"" + " \
                ORDER BY total DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, name=bar_name)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['total'] = float(result[i]['total'])
        return result

# Top 10 beers in a given bar        
def get_top_beers(bar_name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT t1.Beername, COUNT(t1.BeerName) AS total \
                FROM (SELECT TRIM(LEADING '(' FROM SUBSTRING_INDEX(items, ',', 1)) AS BeerName, date \
                FROM BBDext.Bills \
                WHERE bar =  " + "\"" +bar_name +"\"" + ") AS t1 \
                GROUP BY BeerName \
                ORDER BY total DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, name=bar_name)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['total'] = float(result[i]['total'])
        return result

