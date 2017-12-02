from controller_container import ControllerContainer
from model_general_container import ModelGeneralContainer


class ControllerGeneralContainer(ControllerContainer):

    def __init__(self):
        self.associated_container = ModelGeneralContainer()
