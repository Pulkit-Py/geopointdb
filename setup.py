from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="geopointdb",
    version="1.0.0",  # First stable release
    author="Pulkit-Py",
    author_email="pulkitsaini127@gmail.com",
    description="Fast offline city latitude/longitude finder using SQLite database (~200000+ world cities).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pulkit-Py/geopointdb",
    project_urls={
        "Bug Tracker": "https://github.com/Pulkit-Py/geopointdb/issues",
        "Documentation": "https://github.com/Pulkit-Py/geopointdb#readme",
        "Source Code": "https://github.com/Pulkit-Py/geopointdb",
    },
    keywords=[
        "geolocation",
        "latitude",
        "longitude",
        "cities",
        "world cities",
        "offline geocoding",
        "sqlite",
        "coordinates",
        "latlon",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
        ],
    },
    include_package_data=True,
)
