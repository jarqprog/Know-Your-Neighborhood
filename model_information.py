
class ModelInformation():

    def __init__(self):
        self.administrative_division = {}
        self.number_of_occurrences_of_the_locations = {}
        self.counties_with_communities = {}
        self.cities_names = []

    def get_administrative_division(self):
        return self.administrative_division

    def get_number_of_occurrences_of_the_locations(self):
        return self.number_of_occurrences_of_the_locations

    def get_cities_names(self):
        return self.cities_names

    def get_counties_with_communities(self):
        return self.counties_with_communities

    def set_administrative_division(self, new_dict):
        self.administrative_division = new_dict

    def set_number_of_occurrences_of_the_locations(self, new_dict):
        self.number_of_occurrences_of_the_locations.update(
                                    sorted(new_dict.items(), key=lambda x: x[1], reverse=True))

    def set_cities_names(self, new_collection_of_names):
        self.cities_names = sorted(new_collection_of_names, key=len, reverse=True)

    def set_counties_with_communities(self, new_elements_to_dict):
        self.counties_with_communities.update(new_elements_to_dict)

    def clear_my_data(self):
        self.administrative_division.clear()
        self.number_of_occurrences_of_the_locations.clear()
        self.counties_with_communities.clear()
        del self.cities_names[:]
