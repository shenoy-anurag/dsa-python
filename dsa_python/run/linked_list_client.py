from dsa_python.data_structures.linked_list import LinkedList

linked_list = LinkedList()
print("Enter the elements to add/link to the list:")
while True:
    item = input("Enter a number to add or enter '-' to remove: ")
    if item == '-':
        removed_node = linked_list.remove()
        print("removed node {} with memory location {}".format(removed_node.item, hex(id(removed_node))))
    else:
        linked_list.add(item)
    print("num_elements: {} linked list: {}".format(linked_list.n, linked_list))
