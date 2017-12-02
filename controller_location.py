from model_location import ModelLocation


class ControllerLocation():

    def create_location(self,
                        location_name,
                        location_genre,
                        location_code):
        return ModelLocation(location_name, location_genre, location_code)
