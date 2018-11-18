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

def get_beers_name():
    with engine.connect() as con:
        rs = con.execute("SELECT name FROM BBDext.Beer;")
        return [row['name'] for row in rs]

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
    with engine.connect() as con:
        rs = con.execute("SELECT DISTINCT drinker From BBDext.Bills;")
        return [row['drinker'] for row in rs]

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

def num_of_transactions(bar_name):
    with engine.connect() as con:
        query = sql.text(
            "(SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Sunday\"" + 
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Monday\"" + 
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Tuesday\"" +
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Wednesday\"" +
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Thursday\"" +
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Friday\"" +
                "ORDER BY time) \
                UNION ALL \
                (SELECT DAYNAME(date) AS day, COUNT(*) AS num_of_trans \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = " + "\"Saturday\"" +
                "ORDER BY time)"
        )

        rs = con.execute(query, name=bar_name)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['num_of_trans'] = float(result[i]['num_of_trans'])
        return result

def get_bar_inventory(bar_name, day):
    with engine.connect() as con:
        query = sql.text(
            "SELECT CONCAT(Total_Beer_sold_on_given_day, \"/\", Total_Quantity_of_Beer) AS fraction \
                FROM \
                (SELECT COUNT(*) AS Total_Beer_sold_on_given_day \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar_name +"\"" + " \
                AND DAYNAME(date) = "+ "\"" + day +"\"" +") AS c1, \
                (SELECT SUM(quantity) AS Total_Quantity_of_Beer \
                FROM BBDext.Sells \
                WHERE bar = " + "\"" + bar_name +"\"" +") AS c2 "
        )

        rs = con.execute(query, name=bar_name, day=day)
        result = rs.first()
        if result is None:
            return None
    return result['fraction']

def get_top_bars(beer, day):
    with engine.connect() as con:
        if day is None:
            query = sql.text(
            "SELECT bar, COUNT(bar) AS total_sales \
                FROM BBDext.Bills \
                WHERE TRIM(LEADING '(' FROM SUBSTRING_INDEX(items, ',', 1)) = "+ "\"" + beer +"\"" + " \
                GROUP BY bar \
                ORDER BY total_sales DESC \
                LIMIT 10;"
            )

            rs = con.execute(query, beer=beer, day=day)
            result = [dict(row) for row in rs]
            for i, _ in enumerate(result):
                result[i]['total_sales'] = float(result[i]['total_sales'])
            return result

        query = sql.text(
            "SELECT bar, COUNT(bar) AS total_sales \
                FROM BBDext.Bills \
                WHERE TRIM(LEADING '(' FROM SUBSTRING_INDEX(items, ',', 1)) = "+ "\"" + beer +"\"" + " \
                AND DAYNAME(date) = " + "\"" + day +"\"" + " \
                GROUP BY bar \
                ORDER BY total_sales DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, beer=beer, day=day)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['total_sales'] = float(result[i]['total_sales'])
        return result

def get_top_drinkers(beer):
    with engine.connect() as con:
        query = sql.text(
            "SELECT t1.drinker, COUNT(t1.drinker) AS total \
                FROM (SELECT TRIM(LEADING '(' FROM SUBSTRING_INDEX(items, ',', 1)) AS BeerName, date, drinker, bar \
                FROM BBDext.Bills ) AS t1 \
                WHERE t1.BeerName = "+ "\"" + beer +"\"" + " \
                GROUP BY t1.drinker \
                ORDER BY total DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, beer=beer)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['total'] = float(result[i]['total'])
        return result

def popular_times(bar):
    with engine.connect() as con:
        query = sql.text(
            "(SELECT CONCAT('12AM') AS time, COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '12:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('1AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '1:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('2AM'), COUNT(*) AS trans_per_hour  \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '2:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('3AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '3:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('4AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '4:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('5AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '5:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('6AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '6:'\
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('7AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = " + "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '7:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('8AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '8:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('9AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '9:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('10AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '10:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('11AM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '11:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'AM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('12PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '12:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('1PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '1:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('2PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '2:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('3PM'), COUNT(*) AS trans_per_hour  \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '3:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('4PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '4:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('5PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '5:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('6PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '6:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('7PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '7:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('8PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '8:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('9PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 2) = '9:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('10PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '10:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time) \
                UNION ALL \
                (SELECT CONCAT('11PM'), COUNT(*) AS trans_per_hour \
                FROM BBDext.Bills \
                WHERE bar = "+ "\"" + bar +"\"" + " \
                AND SUBSTRING(time, 1, 3) = '11:' \
                AND SUBSTRING(time, (LENGTH(time) - 1)) = 'PM' \
                ORDER BY time)"
        )

        rs = con.execute(query, name=bar)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['trans_per_hour'] = float(result[i]['trans_per_hour'])
        return result

def get_top_manf_sales(manf):
    with engine.connect() as con:
        query = sql.text(
            "SELECT b3.city, COUNT(b3.city) AS city_sales \
                FROM BBDext.Beer b1, (SELECT TRIM(LEADING '(' FROM SUBSTRING_INDEX(items, ',', 1)) AS BeerName, bar \
                FROM BBDext.Bills) AS b2 \
                LEFT JOIN BBDext.Bars b3 ON b2.bar = b3.name \
                WHERE b1.name = b2.Beername \
                AND b1.manf = "+ "\"" + manf +"\"" + " \
                GROUP BY b3.city \
                ORDER BY city_sales DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, manf=manf)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['city_sales'] = float(result[i]['city_sales'])
        return result
        
def get_cities_like_manf(manf):
    with engine.connect() as con:
        query = sql.text(
            "SELECT d.city, COUNT(d.city) AS drinkers_like \
                FROM BBDext.Beer b, BBDext.Likes l \
                LEFT JOIN BBDext.Drinker d ON l.drinker = d.name \
                WHERE b.name = l.beer \
                AND b.manf = "+ "\"" + manf +"\"" + " \
                AND d.name IS NOT NULL \
                GROUP BY d.city \
                ORDER BY drinkers_like DESC \
                LIMIT 10;"
        )

        rs = con.execute(query, manf=manf)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['drinkers_like'] = float(result[i]['drinkers_like'])
        return result

def get_drinker_transactions(drinker):
    with engine.connect() as con:
        query = sql.text(
            "SELECT bar, ID, items,date \
                FROM BBDext.Bills \
                WHERE drinker = " + "\"" + drinker +"\"" + " \
                GROUP BY bar \
                ORDER BY STR_TO_DATE( `time`, '%l:%i %p');"
        )

        rs = con.execute(query, drinker=drinker)
        return [dict(row) for row in rs]

# Drinkers most ordered beers
def get_most_ordered_beer(drinker):
    with engine.connect() as con:
        query = sql.text(
            "SELECT B.name, COUNT(B.name) AS beer_ordered \
                FROM BBDext.Bills, BBDext.Beer B \
                WHERE drinker="+ "\"" + drinker +"\"" + " && LOCATE(B.name, Bills.items)>0 \
                GROUP BY B.name \
                ORDER BY beer_ordered desc \
                LIMIT 10"
        )

        rs = con.execute(query, drinker=drinker)
        result = [dict(row) for row in rs]
        for i, _ in enumerate(result):
            result[i]['beer_ordered'] = float(result[i]['beer_ordered'])
        return result

