import requests
from kaiten.resources.Resource import Resource

class PropertyValues(Resource):
    def __init__(self, propertyvalues_params_dict):
        super().__init__(propertyvalues_params_dict)