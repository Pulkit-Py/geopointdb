import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from geopointdb.getpoint import LatLonFinder

finder = LatLonFinder()
print(finder.find_city('Delhi'))
print(finder.get_coordinates('Shamli'))
