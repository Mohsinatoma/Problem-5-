# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:00:50 2022

@author: Mohoshina Toma
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        
        node = Node(data, self.head)
        self.head = node  

    def insert_data(self, data):
        
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None) 
        

    
    def insert_values(self, datalist):
        self.head = None
        for i in datalist:
            self.insert_data(i)
            
    def length_list(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def copy_list(self,l1):
        itr = l1.head
        while itr:
            self.insert_at_begining(itr.data)
            itr = itr.next
    
    def compare_list(self, l2):
        itr = self.head
        itr1 = l2.head
        
        while (itr != None and itr1 != None): 
            if (itr.data != itr1.data):
                return False
            itr = itr.next
            itr1 = itr1.next
        return  (itr == None and itr1 == None)
            

if __name__ == '__main__':
    ll = LinkedList()
    l2 = LinkedList()
    ll.insert_values([1,2,2,1])
    l2.copy_list(ll)
    ll.print()
    l2.print()
    #count = ll.length_list()

    if (ll.compare_list(l2) == True):
        print("true")
    else:
        print("false")
   
    
  
   
    

  
