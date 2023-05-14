"""
------------------------------------------------------------------------
CP164 Lab 08, Task 04
------------------------------------------------------------------------
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import DATA1, fill_code_bst


bst = BST()

fill_code_bst(bst, DATA1)

for value in bst:
    print(value.letter, value.code)
