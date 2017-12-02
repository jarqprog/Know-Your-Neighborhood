
class ModelRoot():

    def __init__(self, ModelMainContainer):
        self.main_container = ModelMainContainer

    def get_container(self):
        return self.main_container

    def get_all_locations(self):
        return self.main_container.get_all_locations()

    def get_all_voivodeships(self):
        return self.main_container.get_voivodeship_container_locations()

    def get_all_counties(self):
        return self.main_container.get_county_container_locations()

    def get_all_communities(self):
        return self.main_container.get_community_container_locations()

    def get_all_cities(self):
        return self.main_container.get_city_container_locations()

    def clear_containers(self):
        self.main_container.clear_my_containers()
