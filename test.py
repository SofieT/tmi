import BST
from Intervaltree import Intervaltree

__author__ = 'robin'

from Punt import Punt
from RedBlackBST import RedBlackBST
from Segment import Segment

punt1 = Punt(1,1,None)
punt2 = Punt(2,1.1 ,None)
punt3 = Punt(0,1.9 , None)
punt4 = Punt(2,2,None)
punt5 = Punt(-1,0,None)
punt6 = Punt(3,2.05,None)
punt7 = Punt(3,-126,None)
punt8 = Punt(1,2.1, None)
punt9 = Punt(2,2,None)
punt10 = Punt(0,1, None)
punt11 = Punt(-1, 10, None)


def test_bst():
    bst = BST()
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

    seg1 = Segment(punt1, punt8, None)
    seg2 = Segment(punt2, punt9, None)
    seg3 = Segment(punt10, punt3, None)
    seg4 = Segment(punt5, punt11, None)
    seg5 = Segment(punt4, punt6, None)

    rb_tree = Intervaltree()
    rb_tree.insert(seg1)
    rb_tree.insert(seg2)
    rb_tree.insert(seg3)
    rb_tree.insert(seg4)
    rb_tree.insert(seg5)

    rb_tree.delete(seg1)
    rb_tree.delete(seg2)
    rb_tree.delete(seg3)
    rb_tree.delete(seg5)
    rb_tree.delete(seg4)
    # rb_tree.put(punt5, Segment(punt5, punt11, None))
    # rb_tree.delete(punt2)
    # rb_tree.delete(punt10)
    # rb_tree.delete(punt1)
    # rb_tree.delete(punt5)
    return

test_RB_tree()