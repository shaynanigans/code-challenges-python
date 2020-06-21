# Python program merge X sorted linked 
# in third linked list using recursion. 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None

# Overwrites default equality/comparison method, used in test
    def __eq__(self, other_list):
        return self.to_string() == other_list.to_string()

    def to_string(self):
        list_string = ''
        temp = self.head
        while temp.next:
            list_string += str(temp.data) + '->'
            temp = temp.next
        list_string += str(temp.data) 
        return list_string

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data, end = '->')
            temp = temp.next
        print(temp.data, end = ' ')

    def append(self, new_data): 
        new_node = Node(new_data) 
        # If the current list is empty, set the new node to the head
        if self.head is None: 
            self.head = new_node 
            return
        
        last = self.head 
        
        # While there are more nodes in this list, continue
        # O(n)
        while last.next: 
            last = last.next
        # Set the new_node to the tail of the list
        last.next = new_node 


class ListMerger(): 
    # O(1^n) -> O(1)
    # Function to merge two sorted linked list. 
    def merge_two_lists(self,head_1, head_2): 
        # create a temp node None 
        temp = None

        # Escape clauses for recursive algorithm
        # If head_1 is empty then return head_2 
        if head_1 is None: 
            return head_2 

        # And vice-versa 
        if head_2 is None: 
            return head_1 

        # If number stored in head_1 is smaller or 
        # equal to the number in head_2 
        if head_1.data <= head_2.data: 
            # assign value in head_1 to temp
            temp = head_1 

            # Call method recursively from here
            temp.next = self.merge_two_lists(head_1.next, head_2) 
            
        # If number stored in head_2 is smaller than
        # the number in head_1
        else: 
            # assign value in head_2 to temp
            temp = head_2 

            # Call method recursively from here
            temp.next = self.merge_two_lists(head_1, head_2.next) 

        # return the temp list. 
        return temp 

    def merge_all_lists(self,list_of_linked_lists):
        merged_list = list_of_linked_lists[0]
        
        no_of_lists = len(list_of_linked_lists)
        # O(n)
        for i in range(1,no_of_lists):
            if list_of_linked_lists[i].head is not None:
                merged_list.head = self.merge_two_lists(merged_list.head, list_of_linked_lists[i].head)

        return merged_list

# Main method, validating method against data/example in problem sheet
if __name__ == '__main__': 
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

    # 2->6 
    list_3 = LinkedList() 
    list_3.append(2) 
    list_3.append(6) 

    listMerger = ListMerger()
    list_of_linked_lists = [list_1, list_2, list_3]
    
    merged_list = listMerger.merge_all_lists(list_of_linked_lists)
    merged_list.print_list()
    