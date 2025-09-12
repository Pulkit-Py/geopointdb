import csv
import sqlite3
import unicodedata
from pathlib import Path

class LatLonFinder:
    def __init__(self, db_file=None, csv_file=None):
        base_path = Path(__file__).parent
        self.db_file = Path(db_file) if db_file else base_path / "worldcities.db"
        if not self.db_file.exists():
            print("⚡ Database not found. Creating from CSV...")
            self._csv_to_sqlite()
        self.conn = sqlite3.connect(self.db_file)
        self.cur = self.conn.cursor()

    def find_city(self, city_name):
        city_name = f"%{city_name.lower()}%"
        self.cur.execute(
            "SELECT city, country, lat, lon FROM cities WHERE LOWER(city) LIKE ?",
            (city_name,)
        )
        rows = self.cur.fetchall()
        return [
            {"city": row[0], "country": row[1], "lat": row[2], "lon": row[3]}
            for row in rows
        ]

    def get_coordinates(self, city_name):
        self.cur.execute(
            "SELECT lat, lon FROM cities WHERE LOWER(city) = ? LIMIT 1",
            (city_name.lower(),)
        )
        row = self.cur.fetchone()
        if row:
            return (row[0], row[1])
        return None

    def close(self):
        self.conn.close()


