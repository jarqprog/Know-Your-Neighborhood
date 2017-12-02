import sys
import os
import time


class View():

    try:
        from msvcrt import getwch as getch

    except ImportError:

        @staticmethod
        def getch():
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        print('\n\npress any key to continue..\n')
        self.getch()

    def empty_lines_decorator(function_to_decorate):
        def wrapper_function(*args):
            blanc_lines_multiplier = 2
            print('\n' * blanc_lines_multiplier)
            return function_to_decorate(*args)
        return wrapper_function

    @empty_lines_decorator
    def display_message(self, message):
        print(message)

    def display_table_from_collection(self, collection, punktors=False):
        if collection:
            print('\n')
            for item in collection:
                if punktors:
                    print('- {}'.format(item))
                else:
                    print(item)

    @empty_lines_decorator
    def take_user_input(self, message_to_display):
        to_continue = True
        while to_continue:
            user_input = input(message_to_display)
            if user_input:
                to_continue = False
                return user_input

    @staticmethod
    def animate_string(speed=0.00005, string=None):
        """
        Display string using pseudo-animating technique.

        speed: determine "animating" speed (float), default: 0.005
        string: string text to display
        """
        if string is None:
            string = "\n\nLoading program...\n\n"
        for char in string:
            sys.stdout.write("%s" % char)
            sys.stdout.flush()
            time.sleep(speed)

    def display_text_with_asci_graphics(self, text_1=None, text_2=None, repeat=10):
        """
        Display text and asci graphisc in pseudo-animating form.

        Parameters:
        text_1, text_2: string (text to display)
        repeat: integer (number of repeats in loop)

        Sample output:
        Loading program... (text_1)
        ***************************2....
        *****************************1..
        *******************************0
        Program loaded ^o^ (text_2)
        """
        self.animate_string(string=text_1)
        for counter in range(repeat, -1, -1):
            string = "{: >25}".format(
                                        str(counter) +
                                        ("......."*counter) + "\n")
            self.animate_string(string=string)
        self.animate_string(string=text_2)
