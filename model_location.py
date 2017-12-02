class ModelLocation():

    def __init__(self, name, genre, code):
        self.name = name
        self.genre = genre
        self.code = code

    def __str__(self):
        return "{} - {}".format(self.name, self.genre)

    def get_name(self):
        return self.name

    def get_genre(self):
        return self.genre

    def get_code(self):
        return self.code

    def set_name(self, new_name):
        self.name = new_name

    def set_genre(self, new_genre):
        self.genre = new_genre

    def set_code(self, new_code):
        self.code = new_code
