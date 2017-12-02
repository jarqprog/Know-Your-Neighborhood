from view import View


class ViewInformation(View):

    def display_list_statistics(self, locations_to_display):
        weight_of_dividing_line = 60
        dividing_line = '-' * weight_of_dividing_line
        for item in locations_to_display:
            print(dividing_line)
            print('| {:4d} | {}'.format(locations_to_display[item], item))

    def display_location_that_belong_to_more_than_one_category(self, locations_to_display):
        weight_of_dividing_line = 60  # -------
        dividing_line = '-' * weight_of_dividing_line
        lines_to_display_on_screen = 23
        max_number_of_lines = 1000
        lines_that_pause_loop = [
                x for x in range(lines_to_display_on_screen, max_number_of_lines, lines_to_display_on_screen)]
        print('\n| {:4s} | {}'.format('cat.', 'location'))  # table's head
        for line, location in enumerate(locations_to_display):
            print(dividing_line)
            print('| {:4d} | {}'.format(locations_to_display[location], location))
            if line in lines_that_pause_loop:
                self.pause()
                self.clear_screen()

    def display_county_with_communities(self, county_name, collection_of_communities):
        self.clear_screen()
        head_to_display = 'County: {}\n\n{}:'.format(county_name.upper(), 'communities')
        self.display_message(head_to_display)
        weight_of_dividing_line = 30
        dividing_line = '-' * weight_of_dividing_line
        print(dividing_line)
        for community in collection_of_communities:
            print('- {}'.format(community))
        print(dividing_line)
        print('{}: {}'.format('total number of communities', len(collection_of_communities)))

    def display_advanced_search_result(self, locations_to_display):
        weight_of_dividing_line = 60
        dividing_line = '-' * weight_of_dividing_line
        lines_to_display_on_screen = 23
        max_number_of_lines = 1000
        lines_that_pause_loop = [
                line for line in range(lines_to_display_on_screen, max_number_of_lines, lines_to_display_on_screen)]
        print('LOCATION - TYPE\n')  # table's head
        for line, location in enumerate(locations_to_display):
            print(dividing_line)
            print('| {}'.format(location))
            if line in lines_that_pause_loop:
                self.pause()
                self.clear_screen()
