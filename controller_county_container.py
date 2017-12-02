from controller_container import ControllerContainer
from model_county_container import ModelCountyContainer


class ControllerCountyContainer(ControllerContainer):

    def __init__(self):
        self.associated_container = ModelCountyContainer()
