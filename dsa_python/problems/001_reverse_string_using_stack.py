"""
    Problem: Reverse the string given below using a stack to read the secret message!
"""

text = '!gge retsae na dnif ot edoc ruoy hguorht "Desire" drow eht gninnur yrT ."desirE fo rorriM" eht deman saw tI ?koob rettoP yrraH tsrif eht ni rorrim eht fo eman eht rebmemer uoy oD !elzzup eht gnivlos no snoitalutargnoC'

"""
    Solution:
"""
from dsa_python.data_structures.list_stack import Stack

s = Stack()


def reverse_string(text):
    for ch in text:
        s.push(ch)

    reversed_string = ''

    # for _ in range(s.size()):
    #     ch = s.pop()
    #     reversed_string += ch

    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string


reversed_string = reverse_string(text=text)
print()
print(reversed_string)

reversed_string = reverse_string(text="eriseD")
print()
print(reversed_string)
