import unittest
from lootbag import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestLootBag(unittest.TestCase):
    '''
    Testing for lootbag.py functions!
    '''

    @classmethod
    def setUpClass(self):
        # Add Global Variables/etc here
        self.bag = LootBag()
        self.bag.addToy("Doll", "Jill")
        self.bag.addToy("Pony", "Stewie")
        self.bag.addToy("Superman", "Stewie")
        self.bag.addToy("Ball", "Stewie")

    @classmethod
    def tearDownClass(self):
        print('tear down class')

    def test_toy_can_be_added_to_bag_and_assigned_to_child(self):
        self.assertIn("Jill", self.bag.children)
        self.assertIn("Doll", self.bag.children['Jill']['toys'])

    def test_toy_can_be_removed_from_childs_bag(self):
        self.bag.removeToy("Pony", "Stewie")
        self.assertNotIn("Pony", self.bag.children['Stewie'])

    def test_ball_cannot_be_removed_from_childs_bag(self):
        self.bag.removeToy("Ball", "Stewie")
        self.assertIn("Ball", self.bag.children['Stewie']['toys'])

    def test_child_name_must_be_specified_on_remove_toy_from_bag(self):
        self.assertRaises(TypeError, self.bag.removeToy, "Doll")

    def test_must_be_able_to_list_all_children_receiving_a_toy(self):
        child_list = self.bag.getChildrenWithToys()
        self.assertIsNotNone(child_list)

    def test_must_be_able_to_list_all_toys_for_a_single_child_given_child_name(self):
        child_toys = self.bag.getSingleChildWithToys('Stewie')
        self.assertIsNotNone(child_toys)

    def test_must_be_able_to_set_delivered_property_for_child(self):
        self.bag.setDelivered("Stewie", True)
        self.assertTrue(self.bag.children['Stewie']['delivered'])

if __name__ == '__main__':
    unittest.main()