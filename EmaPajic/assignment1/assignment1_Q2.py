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
        
def findKthLastElement(head,k): 
    temp1 = head
    temp2 = head
    while k > 0:
        if temp2 == None:
            return temp2
        k -= 1
        temp2 = temp2.next
    
    while temp2 != None:
        temp1 = temp1.next
        temp2 = temp2.next
        
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
