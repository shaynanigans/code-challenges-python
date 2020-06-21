import unittest

from ..merge_linked_lists_python import LinkedList, ListMerger

class MergeLinkedListTest(unittest.TestCase):
    def test_merge_linked_lists(self):
        # TODO: Write test case to validate functionality
        # 1->4->5 
        list_1 = LinkedList() 
        list_1.append(1) 
        list_1.append(4)
        list_1.append(5) 

        # 1->3->4 
        list_2 = LinkedList() 
        list_2.append(1) 
        list_2.append(3) 
        list_2.append(4) 


        # Create expected result : 
        # 1->1->3->4->4->5 
        expected_result = LinkedList() 
        expected_result.append(1) 
        expected_result.append(1) 
        expected_result.append(3) 
        expected_result.append(4) 
        expected_result.append(4)
        expected_result.append(5) 

        list_of_lists = [list_1, list_2]

        solver = ListMerger()

        self.assertEqual(solver.merge_all_lists(list_of_lists), expected_result)


if __name__ == '__main__':
    unittest.main()