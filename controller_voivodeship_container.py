from controller_container import ControllerContainer
from model_voivodeship_container import ModelVoivodeshipContainer


class ControllerVoivodeshipContainer(ControllerContainer):

    def __init__(self):
        self.associated_container = ModelVoivodeshipContainer()
