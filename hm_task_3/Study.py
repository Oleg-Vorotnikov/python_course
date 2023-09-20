class Materials:
    list_materials = []

    def __init__(self, *args):
        self.list_materials = args


class Pupil:
    def __init__(self):
        self.knowledge_list = []

    def take(self, tit_mat):
        self.knowledge_list.append(tit_mat)


class Teacher:
    cnt_pup = 0

    def teach(self, tit_mat: str, *args):

        for item in args:
            self.cnt_pup += 1
            item.take(tit_mat)


progr = Materials('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')

teach1 = Teacher()
pup1 = Pupil()
pup2 = Pupil()
pup3 = Pupil()
pup4 = Pupil()

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
