# GeoPointDB

[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

GeoPointDB is a lightweight Python package for fast offline geolocation lookups. It provides an easy way to find city coordinates (latitude and longitude) using a local SQLite database containing approximately 200000+ world cities.

## Features

- **Offline First**: No internet connection required after installation
- **Fast Lookups**: Uses SQLite for efficient querying
- **Simple API**: Easy-to-use Python interface
- **Minimal Dependencies**: Uses only Python standard library
- **Auto-setup**: Automatically initializes the database on first use

## Installation

You can install GeoPointDB using pip:

```bash
pip install geopointdb
```

## Quick Start

### Basic Usage

```python
from geopointdb.getpoint import LatLonFinder

# Initialize the finder (automatically sets up the database on first run)
finder = LatLonFinder()

# Find cities by name (case-insensitive partial match)
cities = finder.find_city('New York')
for city in cities:
    print(f"{city['city']}, {city['country']}: {city['lat']}, {city['lon']}")

# Get coordinates for a specific city
coordinates = finder.get_coordinates('London')
if coordinates:
    lat, lon = coordinates
    print(f"London coordinates: {lat}, {lon}")

# Don't forget to close the connection when done
finder.close()
```

### Using Context Manager

For better resource management, you can use the context manager pattern:

```python
with LatLonFinder() as finder:
    coords = finder.get_coordinates('Tokyo')
    print(f"Tokyo coordinates: {coords}")
```

## API Reference

### `LatLonFinder` Class

#### `__init__(self, db_file=None, csv_file=None)`
Initialize the finder with optional custom database or CSV file paths.

- `db_file`: Path to SQLite database file (default: `worldcities.db` in package directory)
- `csv_file`: Path to CSV file for initial database creation (if database doesn't exist)

#### `find_city(self, city_name)`
Find cities by name (case-insensitive partial match).

- `city_name`: Full or partial city name to search for
- Returns: List of dictionaries containing city information (city, country, lat, lon)

#### `get_coordinates(self, city_name)`
Get coordinates for a specific city (exact match).

- `city_name`: Exact city name (case-insensitive)
- Returns: Tuple of (latitude, longitude) or None if not found

#### `close(self)`
Close the database connection. Always call this when done with the finder.

## Database

The package includes a SQLite database (`worldcities.db`) with approximately 200000+ world cities. The database is automatically created from the included CSV file on first use if it doesn't exist.

### Database Schema

The `cities` table has the following columns:
- `city`: City name
- `country`: Country name
- `lat`: Latitude (decimal degrees)
- `lon`: Longitude (decimal degrees)

## Development

### Prerequisites

- Python 3.7+
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pulkit-Py/geopointdb.git
   cd geopointdb
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Unix/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

### Running Tests

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For support, please open an issue on the [GitHub repository](https://github.com/Pulkit-Py/geopointdb/issues).

## Acknowledgements

- World cities data from [geonames.org](https://www.geonames.org/)


## Support

If you found this project helpful, consider:
- Giving it a ⭐ on GitHub
- Following me on social media
- Sharing it with others who might find it useful

---
<p align="center">Made with ❤️ by <a href="https://github.com/Pulkit-Py">Pulkit-Py</a> From 🇮🇳 India</p>