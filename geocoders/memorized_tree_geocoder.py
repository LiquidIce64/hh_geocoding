from custom_queue import CustomQueue
from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    __areas = None

    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            data = API.get_areas()
        if MemorizedTreeGeocoder.__areas is None:
            MemorizedTreeGeocoder.__areas = {}
            nodes = CustomQueue()
            nodes.extend(data)
            while nodes:
                node = nodes.pop()
                self.__areas[int(node.id)] = node.name if node.parent_id is None else (
                                           self.__areas[int(node.parent_id)] + ", " + node.name)
                nodes.extend(node.areas)

    def _apply_geocoding(self, area_id: str) -> str:
        return self.__areas[area_id]
