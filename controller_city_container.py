from controller_container import ControllerContainer
from model_city_container import ModelCityContainer


class ControllerCityContainer(ControllerContainer):

    def __init__(self):
        self.associated_container = ModelCityContainer()
