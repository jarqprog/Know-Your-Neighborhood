from model_root import ModelRoot
from view_root import ViewRoot
from dao import Dao
from controller_main_container import ControllerMainContainer
from controller_information import ControllerInformation


class ControllerRoot():

    def __init__(self):
        self.view = ViewRoot()
        self.dao = Dao()
        self.controller_container = ControllerMainContainer()
        self.model_root = ModelRoot(self.controller_container.get_associated_container())
        self.controller_information = ControllerInformation(self.model_root)

    def start(self):
        self.view.display_start_screen()
        self.update_my_controllers_using_data_from_file()
        exit_program = False
        while not exit_program:
            exit_program = self.controller_information.execute_main_menu()
            if exit_program:
                break
            self.view.clear_screen()
            self.update_my_controllers_using_data_from_file(file_name='')
        self.view.display_exit_screen()
        exit()

    def update_my_controllers_using_data_from_file(self, file_name='malopolska.csv'):
        self.model_root.clear_containers()
        self.controller_information.clear_model_information_data()
        data_from_file = self.get_data_from_file(file_name)
        self.controller_container.fill_containers_with_locations(data_from_file)
        self.controller_information.update_data_in_model_information()
        self.view.display_message('loaded new data to system..')
        self.view.pause()

    def get_data_from_file(self, file_name=''):
        file_is_ready = False
        while not file_is_ready:
            if not file_name:
                available_files_info = 'Founded files:\n\nmalopolska.csv\nmazowsze.csv\nmordor.csv\n'
                self.view.display_message(available_files_info)
                file_name = self.view.take_user_input('please type file name for import data ==> ')
            file_exist = True
            file_content_is_correct = True
            self.view.clear_screen()
            file_exist = self.dao.check_if_file_name_is_correct(file_name)
            if file_exist:
                file_content_is_correct = self.dao.check_if_file_content_is_correct(file_name)
                if file_content_is_correct:
                    file_is_ready = True
                    self.dao.set_data_collection_from_file(file_name)
                    self.view.display_message('loaded data from file: {}'.format(file_name))
                    self.view.pause()
                    self.view.clear_screen()
                    break
            self.view.display_message(available_files_info)
            if not file_exist:
                file_name = self.view.take_user_input(
                            file_name + ' - file not found, please type correct file name ==> ')
            elif not file_content_is_correct:
                file_name = self.view.take_user_input(
                            file_name + ' - incorect file data, please type file with correct data ==> ')
        return self.dao.get_data_collection()
