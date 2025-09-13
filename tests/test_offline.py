import unittest
import os
import sys
from pathlib import Path

# Add the parent directory to the path so we can import the package
sys.path.insert(0, str(Path(__file__).parent.parent))
from geopointdb.getpoint import lat_lon_finder

class TestOfflineFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test data before any tests are run."""
        test_data = """city,lat,lng,country,iso2,admin_name,capital,population,population_proper
New York,40.6943,-73.9249,United States,US,New York,,18713220,18713220
London,51.5074,-0.1278,United Kingdom,GB,London,primary,9540576,8908081
"""
        cls.test_file = Path(__file__).parent / 'test_cities.csv'
        with open(cls.test_file, 'w', encoding='utf-8') as f:
            f.write(test_data)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test data after all tests are run."""
        if cls.test_file.exists():
            cls.test_file.unlink()
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.finder = lat_lon_finder(self.test_file)
    
    def test_find_city(self):
        """Test finding a city by name."""
        results = self.finder.find_city('New York')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['city'], 'New York')
    
    def test_get_coordinates(self):
        """Test getting coordinates for a city."""
        coords = self.finder.get_coordinates('London')
        self.assertIsNotNone(coords)
        self.assertEqual(len(coords), 2)
        self.assertAlmostEqual(coords[0], 51.5074, places=4)
        self.assertAlmostEqual(coords[1], -0.1278, places=4)
    
    def test_city_not_found(self):
        """Test behavior when city is not found."""
        results = self.finder.find_city('Nonexistent City')
        self.assertEqual(len(results), 0)
        coords = self.finder.get_coordinates('Nonexistent City')
        self.assertIsNone(coords)

if __name__ == '__main__':
    unittest.main()
