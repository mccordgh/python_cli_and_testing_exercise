class LootBag(object):
    '''
    Class for the LootBag which contains children and the toys assigned to them
    '''

    def __init__(self):
        self.children = {}

    def addToy(self, toy, child):
        child_exists = self.does_child_exist(child)

        if child_exists:
            self.children[child].append(toy)
        else:
            self.children.update({child : [toy]})

    def does_child_exist(self, child):
        child_exists = False

        for key in self.children:
            if key == child:
                child_exists = True

        return child_exists

    def does_toy_exist(self, toy, child):
        toy_exists = False

        for toys in self.children[child]:
            if toys == toy:
                toy_exists = True

        return toy_exists

    def get_children_with_toys(self):
        children_with_toys = ""

        for key in self.children:
            children_with_toys += "\n{}:".format(key)
            for toy in self.children[key]:
                children_with_toys += "\n\t\t{}".format(toy)
        return children_with_toys

    def removeToy(self, toy, child):
        child_exists = self.does_child_exist(child)

        if child_exists and toy != 'Ball':
            toy_exists = self.does_toy_exist(toy, child)
            if toy_exists:
                self.children[child].remove(toy)
            else:
                print("{} is not in {}'s list of toys!".format(toy, child))
        else:
            print('{} is not in our list of children!'.format(child))

bag = LootBag()

bag.addToy('Pony', "Henry")
print(bag.children)
bag.addToy('HeMan', 'Henry')
print(bag.children)
bag.addToy('Hot Wheels', 'Henry')
print(bag.children)
bag.removeToy('HeMan', 'Henry')
print(bag.children)
bag.removeToy('Giraffe', 'Susan')
bag.removeToy('Giraffe', 'Henry')
print(bag.get_children_with_toys())