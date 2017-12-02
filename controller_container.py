from model_container import ModelContainer


class ControllerContainer():

    associated_container = ModelContainer()

    def add_location(self, ModelLocation):
        self.associated_container.add_location(ModelLocation)

    def clear_locations(self):
        self.associated_container.clear_locations()

    def get_associated_container(self):
        return self.associated_container

    def get_all_locations(self):
        return self.associated_container.get_all_locations()
