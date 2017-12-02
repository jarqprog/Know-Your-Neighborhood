from controller_location import ControllerLocation
from model_main_container import ModelMainContainer
from controller_general_container import ControllerGeneralContainer
from controller_voivodeship_container import ControllerVoivodeshipContainer
from controller_county_container import ControllerCountyContainer
from controller_community_container import ControllerCommunityContainer
from controller_city_container import ControllerCityContainer


class ControllerMainContainer():

    def __init__(self):
        self.controller_location = ControllerLocation()
        self.controller_general_container = ControllerGeneralContainer()
        self.controller_voivodeship_container = ControllerVoivodeshipContainer()
        self.controller_county_container = ControllerCountyContainer()
        self.controller_community_container = ControllerCommunityContainer()
        self.controller_city_container = ControllerCityContainer()

        self.associated_container = ModelMainContainer(
                                    self.controller_general_container.get_associated_container(),
                                    self.controller_voivodeship_container.get_associated_container(),
                                    self.controller_county_container.get_associated_container(),
                                    self.controller_community_container.get_associated_container(),
                                    self.controller_city_container.get_associated_container())

    def get_associated_container(self):
        return self.associated_container

    def create_single_location(self, name, genre, code):
        return self.controller_location.create_location(name, genre, code)

    def fill_containers_with_locations(self, data_from_file):
        for line in data_from_file:
            _name = line[4]
            _genre = line[5]
            _code = line[:4]
            _location = self.create_single_location(_name, _genre, _code)
            self.controller_general_container.add_location(_location)
            if _location.genre == 'miasto':
                self.controller_city_container.add_location(_location)
            if _location.genre == 'województwo':
                self.controller_voivodeship_container.add_location(_location)
            elif _location.genre == 'powiat':
                self.controller_county_container.add_location(_location)
            elif 'gmina' in _location.genre:
                self.controller_community_container.add_location(_location)

    def clear_main_container_data(self):
        self.associated_container.clear_my_containers()
