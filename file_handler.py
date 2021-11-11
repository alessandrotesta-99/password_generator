import os


class file_handler:

    def __init__(self):
        self.file_open = False
        self.name = 0
        self.file = None

    def create_file(self, name):
        if not self.file_open:
            return self.open_file(name, "w")
        else:
            return self.open_file(name, "a")

    def open_file(self, name, mode):
        if mode == "r" and not os.path.exists(name):
            raise Exception("The file can't opened in read mode. The file doesn't exists")
        self.file = open(name, mode)
        self.file_open = True
        self.name = name
        return self.file

    def close_file(self):
        self.file_open = False
        self.file.close()

    def write_file(self, text):
        self.file.write(text)

    def remove_file(self, name):
        if os.path.exists(name):
            os.remove(name)
            self.file = 0
            self.file_open = False

    def print_file(self):
        pass
