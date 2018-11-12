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
    return

def get_bars_selling(beer):
    return

def get_bar_frequent_counts():
    return

def get_bar_cities():
    return

def get_beers():
    return

def get_beer_manufacturers(beer):
    return

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