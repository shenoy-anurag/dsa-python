from dsa_python.data_structures.doubly_linked_linked_list import DoublyLinkedList

doubly_linked_list = DoublyLinkedList()
print("Enter the elements to add/link to the list:")
while True:
    item = input("Enter a number to add or enter '-' to remove: ")
    if item == '-':
        node = doubly_linked_list.remove()
        print("removed node {} with neighbours {} (prev) & {} (next) memory location {}".format(
            node.item,
            node.prev.item if node.prev else None,
            node.next.item if node.next else None,
            hex(id(node)))
        )
    else:
        doubly_linked_list.add(item)
    print("num_elements: {} linked list: {}".format(
        doubly_linked_list.n, doubly_linked_list))
