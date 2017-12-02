from model_information import ModelInformation
from view_information import ViewInformation


class ControllerInformation():

    def __init__(self, ModelRoot):
        self.model_root = ModelRoot
        self.model_information = ModelInformation()
        self.view = ViewInformation()

    def execute_main_menu(self):
        exit_program = False
        to_continue = True
        choices = [
                    "(1) List statistics",
                    "(2) Display 3 cities with longest names",
                    "(3) Display county's name with the largest number of communities",
                    "(4) Display communities for given county",
                    "(5) Display locations, that belong to more than one category",
                    "(6) Advanced search",
                    "(7) Load data from another file",
                    "(0) Exit program"]

        while to_continue:
            self.view.clear_screen()
            self.view.display_table_from_collection(choices)
            correct_choices = [str(number) for number in range(len(choices))]
            user_input_is_correct = False
            while not user_input_is_correct:
                user_input = self.view.take_user_input("What do You want to do? ==> ")
                if user_input in correct_choices:
                    user_input_is_correct = True
            self.view.clear_screen()
            if user_input == '0':
                exit_program = True
                to_continue = False
            elif user_input == '1':
                self.show_list_statistics()
            elif user_input == '2':
                self.show_cities_with_longest_names()
            elif user_input == '3':
                self.show_county_with_the_largest_number_of_communities()
            elif user_input == '4':
                self.show_communities_for_given_county()
            elif user_input == '5':
                self.show_location_that_belong_to_more_than_one_category()
            elif user_input == '6':
                self.execute_advanced_search()
            elif user_input == '7':
                to_continue = False
            if user_input not in ['0', '7']:
                self.view.pause()
        return exit_program

    def update_data_in_model_information(self):
        self.clear_model_information_data()
        self.set_administrative_division()
        self.set_number_of_occurrences_of_the_locations()
        self.set_cities_names()

    def set_administrative_division(self):
        tmp = {}
        for location in self.model_root.get_all_locations():
            if location.genre not in tmp:
                tmp.update({location.genre: 1})
            else:
                tmp[location.genre] += 1
        self.model_information.set_administrative_division(tmp)

    def set_number_of_occurrences_of_the_locations(self):
        tmp = {}
        for location in self.model_root.get_all_locations():
            if location.name not in tmp:
                tmp.update({location.name: 1})
            else:
                tmp[location.name] += 1
        self.model_information.set_number_of_occurrences_of_the_locations(tmp)

    def set_cities_names(self):
        self.model_information.set_cities_names([city.name for city in self.model_root.get_all_cities()])

    def set_counties_with_communities(self):
        counties = self.model_root.get_all_counties()
        communities = self.model_root.get_all_communities()
        counties_with_communities = {}
        county_position_in_code = 1
        for county in counties:
            county_id = county.get_code()[county_position_in_code]
            counties_with_communities.update(
                        {county.name:
                            [community.name for community in communities if community.get_code()[
                                                            county_position_in_code] == county_id]})
        self.model_information.set_counties_with_communities(counties_with_communities)

    def clear_model_information_data(self):
        self.model_information.clear_my_data()

    def show_cities_with_longest_names(self, number_of_cities_to_show=3):
        self.view.display_message('{} cities with longest names:'.format(number_of_cities_to_show))
        cities = self.model_information.get_cities_names()
        self.view.display_table_from_collection(cities[:number_of_cities_to_show], punktors=True)

    def show_county_with_the_largest_number_of_communities(self):
        if not self.model_information.get_counties_with_communities():
            self.set_counties_with_communities()
        counties_with_communities = self.model_information.get_counties_with_communities()
        county_with_biggest_number_of_communities = max(
            counties_with_communities.keys(), key=lambda k: len(counties_with_communities[k]))
        self.view.display_message('County with the largest number of communities:')
        self.view.display_county_with_communities(
                                        county_with_biggest_number_of_communities,
                                        counties_with_communities[county_with_biggest_number_of_communities])

    def show_communities_for_given_county(self):
        if not self.model_information.get_counties_with_communities():
            self.set_counties_with_communities()
        counties_with_communities = self.model_information.get_counties_with_communities()
        user_choice_is_correct = False
        max_number_of_wrong_inputs = 5
        for chances in range(max_number_of_wrong_inputs):
            chosen_county = self.view.take_user_input('Type county name ==> ')
            if chosen_county in counties_with_communities:
                user_choice_is_correct = True
                break
            else:
                self.view.display_message('not found: {}..'.format(chosen_county))
        if user_choice_is_correct:
            self.view.display_county_with_communities(
                                            chosen_county,
                                            counties_with_communities[chosen_county])

    def show_location_that_belong_to_more_than_one_category(self):
        self.view.display_message('Locations, that belong to more than one category:')
        locations = self.model_information.get_number_of_occurrences_of_the_locations()
        self.view.display_location_that_belong_to_more_than_one_category(
                                {key: value for key, value in locations.items() if value > 1})

    def show_list_statistics(self):
        voivodeship_name = self.model_root.get_all_voivodeships()[0].name
        self.view.display_message('list statistics for {}:'.format(voivodeship_name))
        self.view.display_list_statistics(self.model_information.get_administrative_division())

    def execute_advanced_search(self):
        locations = self.model_root.get_all_locations()
        matched_locations = []
        user_input = ''
        self.view.display_message('Advanced search:')
        while not user_input.isalpha():
            user_input = self.view.take_user_input('What should i look for? ==> ')
        length = len(user_input)
        for location in locations:
            if length <= len(location.name):
                if user_input.lower() in location.name.lower()[:length]:
                    matched_locations.append(str(location))
        matched_locations.sort()
        self.view.clear_screen()
        self.view.display_message('Searching for: "{}"'.format(user_input))
        self.view.pause()
        self.view.clear_screen()
        self.view.display_message('Found {} location(s)\n\n'.format(len(matched_locations)))
        self.view.display_advanced_search_result(matched_locations)
