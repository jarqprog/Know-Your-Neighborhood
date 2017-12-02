class ModelMainContainer():

    def __init__(
                    self,
                    ModelGeneralContainer,
                    ModelVoivodeshipContainer,
                    ModelCountyContainer,
                    ModelCommunityContainer,
                    ModelCityContainer):

        self.general_container = ModelGeneralContainer
        self.voivodeship_container = ModelVoivodeshipContainer
        self.county_container = ModelCountyContainer
        self.community_container = ModelCommunityContainer
        self.city_container = ModelCityContainer

    def get_all_locations(self):
        return self.general_container.get_all_locations()

    def get_voivodeship_container_locations(self):
        return self.voivodeship_container.get_all_locations()

    def get_county_container_locations(self):
        return self.county_container.get_all_locations()

    def get_community_container_locations(self):
        return self.community_container.get_all_locations()

    def get_city_container_locations(self):
        return self.city_container.get_all_locations()

    def clear_my_containers(self):
        self.general_container.clear_locations()
        self.voivodeship_container.clear_locations()
        self.county_container.clear_locations()
        self.community_container.clear_locations()
        self.city_container.clear_locations()
