import sys
import json


def setUpBools(data):
    for key in data:
        for child in data[key]:
            if child == 'delivered':
                if data[key]['delivered'] == 'False':
                    data[key]['delivered'] = False
                if data[key]['delivered'] == 'True':
                    data[key]['delivered'] = True
    return data

def loadChildren():
    with open("santas_list.json") as santa_file:
        data = setUpBools(json.load(santa_file))
        return data

def saveAll(data):
    with open('santas_list.json', 'w') as outfile:
        json.dump(data, outfile)

class LootBag(object):
    '''
    Class for the LootBag which contains children and the toys assigned to them
    '''

    def __init__(self):
        self.children = loadChildren()

    def addToy(self, toy, child):
        '''add [toy] [child] :: Add Toy to a child's list of toys, if child does not exist then create it in bag.children
        
        Keyword Arguments:
        toy -- name of the toy
        child -- name of the child        
        '''

        child_exists = self.doesChildExist(child)

        if child_exists:
            self.children[child]['toys'].append(toy)
        else:
            self.children.update({child : { 'delivered' : False, 'toys' : [toy]}})

    def doesChildExist(self, child):
        '''childexists [child] :: Return True if child exists in bag.children, False if not

        Keyword Arguments:
        child -- name of the child        
        '''

        child_exists = False

        for key in self.children:
            if key == child:
                child_exists = True

        return child_exists

    def doesToyExist(self, toy, child):
        '''toyexists [toy] [child] :: Return True if toy exists in bag.children[child], False if not

        Keyword Arguments:
        toy -- name of the toy
        child -- name of the child        
        '''

        toy_exists = False

        for toys in self.children[child]['toys']:
            if toys == toy:
                toy_exists = True

        return toy_exists

    def getChildrenWithToys(self):
        '''getall :: Returns a string ready for printing of all children and their assigned toys
        '''

        children_with_toys = ""

        for key in self.children:
            children_with_toys += "\n{}:\n\tdelivered: {}".format(key, self.children[key]['delivered'])
            for toy in self.children[key]:
                 if toy == 'toys':
                    children_with_toys += "\n\ttoys:\t {}".format(', '.join(self.children[key][toy]))
        return children_with_toys

    def getSingleChildWithToys(self, child):
        '''getchild [child] :: Returns a string ready for printing of a single child and their assigned toys

        Keyword Arguments:
        child -- name of the child        
        '''

        if self.doesChildExist(child):
            child_with_toys = ""

            for key in self.children:
                if key == child:
                    child_with_toys += "\n{}:\n\tdelivered: {}".format(key, self.children[key]['delivered'])
                    for toy in self.children[key]:
                        if toy == 'toys':
                            child_with_toys += "\n\ttoys:\t {}".format(", ".join(self.children[key][toy]))

            return child_with_toys
        else:
            return None

    def isDelivered(self, child):
        '''isdelivered [child] :: Returns True if the child's delivered flag == True, False if it == False

        Keyword Arguments:
        child -- name of the child        
        '''
        child_exists = self.doesChildExist(child)
        if child_exists:
            is_delivered = bag.children[child]['delivered']
            if is_delivered:
                print("{}'s toys have been delivered!".format(child))
            else:
                print("{}'s toys have NOT been delivered!".format(child))
        else:
            print('{} is not in our list of children!'.format(child))

    def removeToy(self, toy, child):
        '''remove [toy] [child] :: Remove a toy from a child's list

        Keyword Arguments:
        toy -- name of the toy
        child -- name of the child        
        '''

        child_exists = self.doesChildExist(child)

        if toy == 'Ball':
            print("Not allowed to remove Ball from list")
            return

        if child_exists:
            toy_exists = self.doesToyExist(toy, child)
            if toy_exists:
                self.children[child]['toys'].remove(toy)
            else:
                print("{} is not in {}'s list of toys!".format(toy, child))
        else:
            print('{} is not in our list of children!'.format(child))

    def setDelivered(self, child, delivered_bool):
        '''setdelivered [child] [true/false] :: Sets the childs delivered flag to True or False
            
        Keyword Arguments:
        child -- name of the child        
        delivered_bool -- True or False
        '''

        if self.doesChildExist(child):
            self.children[child]['delivered'] = delivered_bool
        else:
            print('{} is not in our list of children!'.format(child))

bag = LootBag()

def arg_parser(args=['meh']):
    data_altered = False
    cli_command = ""
    if len(args) > 0:
        cli_command = str(args[0]).lower()
    else:
        print("Please supply a command. Type 'help' for a list of commands")
    if  cli_command == 'add':
        if len(args) > 2:
            bag.addToy(args[1], args[2])
            data_altered = True
        else:
            print("please supply a toy name, and a child name")

    if cli_command == 'childexists':
        if args[1]:
            if bag.doesChildExist(args[1]):
                print("{} does exist".format(args[1]))
            else:
                print("{} does NOT exist".format(args[1]))

    if cli_command == 'exit':
        saveAll(bag.children)

    if cli_command == 'getall':
        print(bag.getChildrenWithToys())

    if cli_command == 'getchild':
        if args[1]:
            print(bag.getSingleChildWithToys(args[1]))
        else:
            print("Please supply a child's name")

    if cli_command == 'isdelivered':
        if args[1]:
            bag.isDelivered(args[1])

    if  cli_command == 'remove':
        if args[1] and args[2]:
            bag.removeToy(args[1], args[2])
            data_altered = True
        else:
            print("please supply a toy name, and a child name")    

    if cli_command == 'setdelivered':
        print(args)
        if args[1] and args[2]:
            if args[2] == 'True':
                bag.setDelivered(args[1], True)
                print("{}'s delivered flag set to True".format(args[1]))
                data_altered = True
            if args[2] == 'False':
                bag.setDelivered(args[1], False)
                print("{}'s delivered flag set to False".format(args[1]))
                data_altered = True
    
        if not data_altered:
            print("Please supply a child name, and True or False argument")

    if cli_command == 'toyexists':
        if args[1] and args[2]:
            if bag.doesToyExist(args[1], args[2]):
                print("{} does exist in {}'s toy list".format(args[1], args[2]))
            else:
                print("{} does NOT exist in {}'s toy list".format(args[1], args[2]))

    if cli_command == 'help' or cli_command == '?':
        print("lootbag.py Documentation:\n")
        print(bag.addToy.__doc__)
        print(bag.doesChildExist.__doc__)
        print(bag.getChildrenWithToys.__doc__)
        print(bag.getSingleChildWithToys.__doc__)
        print(bag.isDelivered.__doc__)
        print(bag.removeToy.__doc__)
        print(bag.setDelivered.__doc__)
        print(bag.doesToyExist.__doc__)

    if data_altered:
        saveAll(bag.children)

if __name__ == '__main__':
    arg_parser(sys.argv[1:])

