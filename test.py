__author__ = 'robin'

from BST import Searchtree
from Punt import Punt
from RedBlackBST import RedBlackBST
from Segment import Segment

punt1 = Punt(1,1,None)
punt2 = Punt(2,1,None)
punt3 = Punt(0,2, None)
punt4 = Punt(2,2,None)
punt5 = Punt(-1,0,None)
punt6 = Punt(3,162,None)
punt7 = Punt(3,-126,None)
punt8 = Punt(1,2, None)
punt9 = Punt(2,2,None)
punt10 = Punt(0,1, None)
punt11 = Punt(-1, 10, None)


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
    rb_tree.put(punt10, Segment(punt10, punt3, None))
    rb_tree.put(punt5, Segment(punt5, punt11, None))
    rb_tree.delete(punt10)
    return

test_RB_tree()