import csv


class Dao():

    def __init__(self):
        self.data_collection = []

    def check_if_file_name_is_correct(self, file_name):
        try:
            with open(file_name, 'r', encoding="utf8"):
                return True
        except:
            return False

    def check_if_file_content_is_correct(self, file_name):
        try:
            with open(file_name, 'r', encoding="utf8") as file:
                _tmp = list(csv.reader(file, delimiter='\t'))
                for line in _tmp:
                    if not line[4] or not line[5] or not line[0]:
                        return False
                return True
        except:
            return False

    def set_data_collection_from_file(self, file_name):
        with open(file_name, 'r', encoding="utf8") as file:
            next(file)
            self.data_collection = list(csv.reader(file, delimiter='\t'))

    def get_data_collection(self):
        return self.data_collection



