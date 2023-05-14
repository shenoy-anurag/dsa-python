# import sys
# sys.path.append('.')

from dsa_python.data_structures.linked_stack import LinkedStack

stack = LinkedStack()
print("Enter the elements to push onto to the stack:")
while True:
    item = input("Enter a number to push or enter '-' to pop: ")
    if item == '-':
        popped_value = stack.pop()
        print("Popped value: {}".format(popped_value))
    else:
        stack.push(item)
    print("Current stack: {}".format(stack))
