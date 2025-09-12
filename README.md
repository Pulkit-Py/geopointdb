# README.md

# geopointdb

geopointdb is an offline geolocation and geocoding package that allows users to retrieve geographical information about cities around the world. It provides a simple interface for accessing city data and performing geolocation tasks without the need for an internet connection.

## Features

- Access to a comprehensive dataset of world cities.
- Offline geolocation and geocoding capabilities.
- Command-line interface for easy interaction.
- Fast local lookups with a small memory footprint.
- Simple Python API for integration in scripts and services.

## Usage

CLI
- Run the bundled command-line interface:
  - Windows: python -m geopointdb.cli
  - Or: python -m geopointdb.cli --help

Python (example)
- Import the package and use the provided API (example API shown as illustration — consult the package docs for exact names):
```py
from geopointdb import GeoPointDB

db = GeoPointDB("path/to/data")
result = db.lookup_city("Paris")
print(result)
```

## Development

Get the repo and create a dev environment (Windows example):
```powershell
git clone https://github.com/Pulkit-Py/geopointdb
cd geopointdb
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

Run tests:
```powershell
pytest
```

Contributing
- Please open issues for bugs or feature requests.
- Submit pull requests for proposed fixes or improvements.
- Follow the existing code style and add tests for new functionality.

## Package information

- Package name: geopointdb
- Current version: 0.1.0 (placeholder — see package metadata)
- Supported Python: >=3.8

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Pulkit (GitHub: Pulkit-Py)

## Support

If you found this project helpful, consider:
- Giving it a ⭐ on GitHub
- Following me on social media
- Sharing it with others who might find it useful

---
<p align="center">Made with ❤️ by <a href="https://github.com/Pulkit-Py">Pulkit-Py</a> From 🇮🇳 India</p>