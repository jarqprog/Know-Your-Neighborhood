from view import View


class ViewRoot(View):

    def display_start_screen(self):
        self.clear_screen()
        self.display_text_with_asci_graphics(
                                text_1='\n\n\nLoading program...\n\n',
                                text_2='\n\t\t\t...loaded\n')

        title = "\n\t\t{}\n\t\t\t\t{}".format(
                                "Welcome to 'Know your neighbourhood' program by jq...",
                                "with Frodo's guide add-on")
        self.animate_string(string=title)
        self.pause()

    def display_exit_screen(self):
        self.clear_screen()
        self.display_text_with_asci_graphics(
                                text_1='\n\n\nLeaving the app...\n',
                                text_2='\nThank You 4 using me, bye! :)\n\n\n')
