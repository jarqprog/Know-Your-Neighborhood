
class ModelContainer():

    locations = []

    def add_location(self, ModelLocation):
        self.locations.append(ModelLocation)

    def clear_locations(self):
        del self.locations[:]

    def get_all_locations(self):
        return self.locations
