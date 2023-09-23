class People:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex


class Materials:
    list_materials = []

    def __init__(self, *args):
        self.list_materials = args

    def __len__(self):
        return len(self.list_materials)


class Pupil(People):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.knowledge_list = []

    def take(self, tit_mat):
        self.knowledge_list.append(tit_mat)

    def __len__(self):
        return len(self.knowledge_list)

    def rem_knowledge(self, knowledge):
        self.knowledge_list.remove(knowledge)


class Teacher(People):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.cnt_pup = 0

    def teach(self, tit_mat: str, *args):
        for item in args:
            self.cnt_pup += 1
            item.take(tit_mat)


progr = Materials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')

teach1 = Teacher('Maria', 'Ivanovna', 47, 'female')
pup1 = Pupil('Ivan', 'Ivanov', 15, 'male')
pup2 = Pupil('Petr', 'Petrov', 14, 'male')
pup3 = Pupil('Anna', 'Smirnova', 14, 'female')
pup4 = Pupil('Maria', 'Sidorova', 15, 'female')

teach1.teach(progr.list_materials[0], pup1, pup2, pup3, pup4)
teach1.teach(progr.list_materials[1], pup1, pup3, pup4)
teach1.teach(progr.list_materials[2], pup3, pup4)
teach1.teach(progr.list_materials[3], pup1, pup2, pup3)
teach1.teach(progr.list_materials[4], pup1, pup4)

print(pup1.knowledge_list)
print(pup2.knowledge_list)
print(pup3.knowledge_list)
print(pup4.knowledge_list)
print(teach1.cnt_pup)

print(len(pup3))
print(len(progr))
print(pup1.first_name, pup1.last_name)

pup2.rem_knowledge('NoSQL databases')
print(pup2.knowledge_list)
