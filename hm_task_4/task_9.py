import csv
import re
from collections import Counter


class ai_data:
    def __init__(self, path_file):
        self.path_file = path_file
        self.list_data = []

    def read_file(self):
        with open(self.path_file, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            headers = next(file_reader)
            for row in file_reader:
                self.list_data.append(row)

        return self.list_data

    def comp_free_review(self):
        cnt_free = 0
        cnt_other = 0
        for line in self.list_data:

            if line[2] == 'Free' and line[5]:
                cnt_free += 1
            elif line[5]:
                cnt_other += 1

        if cnt_free > cnt_other:
            print("Обзоров больше на бесплатные инструменты", cnt_free, cnt_other)
        elif cnt_free == cnt_other:
            print("Обзоров одинаковое количество", cnt_free, cnt_other)
        else:
            print("Обзоров больше на платные инструменты", cnt_free, cnt_other)

    def most_common_Use_for(self):
        list_date = []
        for line in self.list_data:
            if line[2] == 'Free':
                list_date.append(line[3])

        return Counter(list_date).most_common(1)

    #def top_instr(self, top_app=None, top_task=None, top_cat=None):
        #if top_app:
            #if top_app == 'Free':
              #  list_free = []

         #   else:
          #      list_paid = []
    # Не очень понятно задание g, топ-3 по какому критерию?


ai_obj = ai_data('all_ai_tool.csv')
ai_obj.read_file()
ai_obj.comp_free_review()
print(ai_obj.most_common_Use_for())
