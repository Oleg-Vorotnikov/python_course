# import numpy as np
import re


class Mess_file:
    def __init__(self, path_file: str):
        self.path_file = path_file
        self.list_array = []

    def read_array(self):
        with open(self.path_file, "r") as f:        # С произвольным текстом
            for line in f:                          # np.genfromtxt не работает
                self.list_array.append(line)

    def search_patr(self, my_patr):
        res_list = []
        for line in self.list_array:
            result = re.search(my_patr, line)
            if result:
                res_list.append(result.group())
        return res_list


mess_obj = Mess_file("text_pr6.txt")
mess_obj.read_array()
print(mess_obj.list_array)
print(mess_obj.search_patr(r'\d{2}'))
