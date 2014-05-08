from RedBlackBST import RedBlackBST
from Segment import Segment

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
punt8 = Punt(1,2, None)
punt9 = Punt(2,2,None)


def test_bst():
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

def test_RB_tree():
    rb_tree = RedBlackBST()
    rb_tree.put(punt1, Segment(punt1, punt8, None))
    rb_tree.put(punt2, Segment(punt2, punt9, None))
    return

test_RB_tree()