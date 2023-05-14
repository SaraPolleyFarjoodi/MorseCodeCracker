"""
------------------------------------------------------------------------
CP164 Lab 08, Task 06
------------------------------------------------------------------------
------------------------------------------------------------------------
"""
# Task 7 is just for self study (No answer needed)
from BST_linked import BST
from morse import DATA1, fill_code_bst, decode_morse

bst = BST()

fill_code_bst(bst, DATA1)

text = "... --- ..."

print(decode_morse(bst, text))
