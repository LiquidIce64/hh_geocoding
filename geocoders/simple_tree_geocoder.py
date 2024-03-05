from custom_queue import CustomQueue
from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    __data = None

    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            data = API.get_areas()
        if SimpleTreeGeocoder.__data is None:
            nodes = CustomQueue()
            for node in data:
                node.parent = None
                nodes.push(node)
            while nodes:
                node = nodes.pop()
                for area in node.areas:
                    area.parent = node
                    nodes.push(area)
            SimpleTreeGeocoder.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        nodes = CustomQueue()
        nodes.extend(self.__data)
        while nodes:
            node = nodes.pop()
            if int(node.id) == area_id: break
            nodes.extend(node.areas)
        else:
            raise LookupError(area_id)
        result = node.name
        while node.parent is not None:
            node = node.parent
            result = node.name + ", " + result
        return result
