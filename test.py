__author__ = 'robin'

from BST import Searchtree
from Punt import Punt
from Algorithms import Algo2

punt1 = Punt(1,1,None)
punt2 = Punt(2,1,None)
punt3 = Punt(0,2, None)
punt4 = Punt(2,2,None)
punt5 = Punt(-1,0,None)
punt6 = Punt(3,162,None)
punt7 = Punt(3,-126,None)

bst = Searchtree()
bst.insert(punt1)
bst.insert(punt2)
bst.insert(punt5)
bst.insert(punt3)
bst.insert(punt6)
bst.insert(punt4)
bst.insert(punt7)

print(bst.pop())
print(bst.pop())
print(bst.pop())
print(bst.pop())
print(bst.pop())
print(bst.pop())
print(bst.pop())

