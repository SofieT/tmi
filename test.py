import BST
from Intervaltree import Intervaltree

__author__ = 'robin'

from Punt import Punt
from RedBlackBST import RedBlackBST
from Segment import Segment

# punt1 = Punt(1,1,None)
# punt2 = Punt(2,1.1 ,None)
# punt3 = Punt(0,1.9 , None)
# punt4 = Punt(2,2,None)
# punt5 = Punt(-1,0,None)
# punt6 = Punt(3,2.05,None)
# punt7 = Punt(3,-126,None)
# punt8 = Punt(1,2.1, None)
# punt9 = Punt(2,2,None)
# punt10 = Punt(0,1, None)
# punt11 = Punt(-1, 10, None)
#
#
# def test_bst():
#     bst = BST()
#     bst.insert(punt1)
#     bst.insert(punt2)
#     bst.insert(punt5)
#     bst.insert(punt3)
#     bst.insert(punt6)
#     bst.insert(punt4)
#     bst.insert(punt7)
#
#     print(bst.pop())
#     print(bst.pop())
#     print(bst.pop())
#     print(bst.pop())
#     print(bst.pop())
#     print(bst.pop())
#     print(bst.pop())

punt1 = Punt(1,1,None)
punt2 = Punt(1,3,None)
seg1 = Segment(punt1, punt2, None)

punt3 = Punt(1,2,None)
punt4 = Punt(1,5,None)
seg2 = Segment(punt3, punt4, None)

punt5 = Punt(1,4,None)
punt6 = Punt(1,7,None)
seg3 = Segment(punt5, punt6, None)

punt7 = Punt(1,6,None)
punt8 = Punt(1,9,None)
seg4 = Segment(punt7, punt8, None)

punt9 = Punt(1,8,None)
punt10 = Punt(1,11,None)
seg5 = Segment(punt9, punt10, None)

punt11 = Punt(1,10,None)
punt12 = Punt(1,13,None)
seg6 = Segment(punt11, punt12, None)

punt13 = Punt(1,12,None)
punt14 = Punt(1,15,None)
seg7 = Segment(punt13, punt14, None)

punta = Punt(1, 1.5)
puntb = Punt(1, 13.5)
overlapseg = Segment(punta, puntb, None)

def test_interval_tree():
    tree = Intervaltree()
    tree.insert(seg4)
    tree.insert(seg2)
    tree.insert(seg3)
    tree.insert(seg1)
    tree.insert(seg5)
    tree.insert(seg6)
    tree.insert(seg7)
    overlaps = tree.searchOverlap(overlapseg)

    return
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
    rb_tree.delete(seg4)
    rb_tree.delete(seg5)
    return

test_interval_tree()