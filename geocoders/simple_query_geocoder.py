from api import API
from geocoders.geocoder import Geocoder


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        node = API.get_area(area_id)
        result = node.name
        while node.parent_id is not None:
            node = API.get_area(node.parent_id)
            result = node.name + ", " + result
        return result
