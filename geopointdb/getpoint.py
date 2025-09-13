import csv
import sqlite3
import unicodedata
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Any, Union
import importlib.resources as pkg_resources

class LatLonFinder:
    """
    A class to find latitude and longitude coordinates for cities using an offline SQLite database.
    
    Args:
        db_file: Path to the SQLite database file. If not provided, uses the default database.
        csv_file: Path to a CSV file to initialize the database if it doesn't exist.
    """
    
    def __init__(self, db_file: Optional[Union[str, Path]] = None, 
                 csv_file: Optional[Union[str, Path]] = None) -> None:
        base_path = Path(__file__).parent
        self.db_file = pkg_resources.files("geopointdb") / "worldcities.db"
        if not self.db_file.exists():
            print("⚡ Database not found. Creating from CSV...")
            self._csv_to_sqlite()
        self.conn = sqlite3.connect(str(self.db_file))
        self.cur = self.conn.cursor()

    def find_city(self, city_name: str) -> List[Dict[str, Any]]:
        """
        Find cities by name (case-insensitive partial match).
        
        Args:
            city_name: Full or partial city name to search for
            
        Returns:
            List of dictionaries containing city information (city, country, lat, lon)
        """
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

    def get_coordinates(self, city_name: str) -> Optional[Tuple[float, float]]:
        """
        Get coordinates for a specific city (exact match).
        
        Args:
            city_name: Exact city name (case-insensitive)
            
        Returns:
            Tuple of (latitude, longitude) if found, None otherwise
        """
        self.cur.execute(
            "SELECT lat, lon FROM cities WHERE LOWER(city) = ? LIMIT 1",
            (city_name.lower(),)
        )
        row = self.cur.fetchone()
        if row:
            return (row[0], row[1])
        return None

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
        
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure the database connection is closed when exiting the context."""
        self.close()
