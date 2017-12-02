from controller_container import ControllerContainer
from model_community_container import ModelCommunityContainer


class ControllerCommunityContainer(ControllerContainer):

    def __init__(self):
        self.associated_container = ModelCommunityContainer()
