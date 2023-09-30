import csv
import re
from collections import Counter


class Ufo_data:
    def __init__(self, path_file):
        self.path_file = path_file
        self.list_data = []

    def read_file(self):
        with open(self.path_file, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            headers = next(file_reader)
            for row in file_reader:
                self.list_data.append(row)

    def most_common_country(self):
        list_country = []
        for line in self.list_data:
            list_country.append(line[3])

        # print(Counter(self.list_dict[0]['country']).most_common(1))

        return Counter(list_country).most_common(1)

    def most_common_month(self):
        list_date = []
        for line in self.list_data:
            result = re.match(r'\d{1,2}', line[0])
            list_date.append(result.group())

        return Counter(list_date).most_common(1)


ufo_obj = Ufo_data('nlo.csv')
ufo_obj.read_file()
print(ufo_obj.most_common_country())
print(ufo_obj.most_common_month())
#print(ufo_obj.read_file())
