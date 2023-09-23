class Apple:
    stages_of_rip = ['flower', 'green', 'red']

    def __init__(self, ind_app):
        self.ind_app = ind_app
        self.stage = self.stages_of_rip[0]

    def apple_ripe(self):
        ind = self.stages_of_rip.index(self.stage)
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
    def __init__(self, *args):
        self.list_apple = []
        for item in args:
            self.list_apple.append(item)

    def tree_growth(self):
        for i in range(0, len(self.list_apple)):
            self.list_apple[i].apple_ripe()

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


app1 = Apple(1)
app2 = Apple(2)
app3 = Apple(3)
app4 = Apple(4)
app5 = Apple(5)
tree1 = Tree(app1, app2, app3, app4, app5)
#tree1.tree_growth()
# tree1.tree_growth()
#print(tree1.stage_all_apple())
#tree1.del_all_apple()
gard1 = Gardener('Ivan', 'Ivanych', tree1)
gard1.growth_all_tree()
gard1.harvest()
gard1.growth_all_tree()
gard1.harvest()
