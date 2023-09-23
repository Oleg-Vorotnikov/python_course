import random


class Apple:
    stages_of_rip = ['flower', 'green', 'red']

    def __init__(self, ind_app):
        self.ind_app = ind_app
        self.stage = self.stages_of_rip[0]
        self.cycle = 1

    def apple_ripe(self):
        ind = self.stages_of_rip.index(self.stage)
        self.cycle += 1
        if ind != 2:
            self.stage = self.stages_of_rip[ind + 1]

    def check_stage(self):
        ind = self.stages_of_rip.index(self.stage)
        if ind == 2:
            return True
        else:
            return False

    def __del__(self):
        print(f'Сорвали яблоко {self.ind_app}')


class Tree:
    def __init__(self, age_tree=1, *args):
        self.list_apple = []
        self.age_tree = age_tree
        if self.age_tree > 2:
            for item in args:
                self.list_apple.append(item)

    def tree_growth(self):
        self.age_tree += 1
        if self.age_tree > 2:
            num_new_apple = 0
            if self.age_tree < 5:
                num_new_apple = random.randint(0, 3)
                for i in range(num_new_apple):
                    new_apple = Apple(len(self.list_apple) + 1)
                    self.list_apple.append(new_apple)
            if self.age_tree in range(3, 5):
                for i in range(len(self.list_apple) - num_new_apple):
                    self.list_apple[i].apple_ripe()
            elif self.age_tree in range(5, 10):
                i = 0
                while i < len(self.list_apple):
                    self.list_apple[i].apple_ripe()
                    if self.list_apple[i].cycle > 5:
                        del self.list_apple[i]
                        i -= 1
                    i += 1
            else:
                self.del_all_apple()

    def stage_all_apple(self):
        for i in range(0, len(self.list_apple)):
            if not self.list_apple[i].check_stage():
                return False

        return True

    def del_all_apple(self):
        while len(self.list_apple) > 0:
            del self.list_apple[0]


class Gardener:
    def __init__(self, first_name, last_name, *args):
        self.first_name = first_name
        self.last_name = last_name
        self.list_tree = []
        for item in args:
            self.list_tree.append(item)

    def growth_all_tree(self):
        for i in range(0, len(self.list_tree)):
            self.list_tree[i].tree_growth()

    def harvest(self):
        for i in range(len(self.list_tree)):
            if not self.list_tree[i].stage_all_apple():
                print(f'Не все яблоки созрели на дереве {i}')
            else:
                self.list_tree[i].del_all_apple()
                print(f'Яблоки собраны с дерева {i}')

    def stat_gard(self):
        for i in range(len(self.list_tree)):
            print(f'Number of Tree: {i + 1}', ' Age: ', self.list_tree[i].age_tree, ' Count of apple: ',
                  len(self.list_tree[i].list_apple))
            for j in range(len(self.list_tree[i].list_apple)):
                print(f'Stage of apple {self.list_tree[i].list_apple[j].ind_app}:',
                      self.list_tree[i].list_apple[j].stage)


app1 = Apple(1)
app2 = Apple(2)
app3 = Apple(3)
# app4 = Apple(4)
# app5 = Apple(5)
tree1 = Tree(3, app1, app2, app3)
tree2 = Tree()
gard1 = Gardener('Ivan', 'Ivanych', tree1, tree2)
gard1.growth_all_tree()
gard1.harvest()
# gard1.stat_gard()
gard1.growth_all_tree()
# gard1.stat_gard()
gard1.growth_all_tree()
# gard1.stat_gard()
gard1.growth_all_tree()
gard1.growth_all_tree()
