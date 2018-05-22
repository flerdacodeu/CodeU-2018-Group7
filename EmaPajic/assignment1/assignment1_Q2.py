#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import sys

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 
        
""" Algorithm to find kth last elemet:
    We have 2 pointers, temp1 and temp2, and at the beginning we set them both to head.
    We move pointer temp2 for k places, if we reach the end of the list during that,that means that the list doesn't have k elements and so we return null
    After that, we are simultaneously moving temp1 and temp2 until temp2 reaches the end of the list. 
    Temp1 is always k places ahead temp2 so when temp2 reaches end of the list temp1 witll be exactly k places before the end of the list.
    We return that node.
"""
def find_kth_last_element(head,k): 
    temp1 = head
    temp2 = head
    # move pointer temp2 k places
    while k >= 0:
        if temp2 == None:
            return temp2
        k -= 1
        temp2 = temp2.next
    
    # move temp1 and temp2 simultaneously
    while temp2 != None:
        temp1 = temp1.next
        temp2 = temp2.next
        
    # return kth last node
    return temp1
       
def main():
    
    head = None
    tail = None
    sys.stdout.write('Input the number of nodes')
    n = int(input())
    sys.stdout.write('Input values of nodes')
    for i in range(0,n):
        val = int(input())
        nd = Node(val)
        if head == None:
            head = nd
        else:
            tail.next = nd
        tail = nd
      
    sys.stdout.write('Input k')
    k = int(input())
    KthLast = findKthLastElement(head,k)
    if KthLast == None:
        sys.stdout.write('K is greater than length of the list')
    else:
        sys.stdout.write('Kth last element is: '+str(KthLast.val))
    
main()
