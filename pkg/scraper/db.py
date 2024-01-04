import sqlite3    

class Database:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS food_data (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, product_url TEXT, quantity TEXT)
            """)
        

    def insert(self, result):
        self.cur.execute("""
            INSERT INTO food_data (name, price, product_url, quantity) VALUES (?,?,?,?)
        """, (result['name'], result['price'], result['product_url'], result['quantity']))

        self.con.commit()


        return True

    def retrive(self):
        res = self.cur.execute("""
            SELECT * FROM food_data
        """)
        res.fetchall()

        return res
