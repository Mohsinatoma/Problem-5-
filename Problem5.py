# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:00:50 2022

@author: Mohoshina Toma
"""

    def reverseList(self,head):
        
        prev = None
        
        while(head != None):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
    
    def isPalindrome(self, head):
      
        if head == None:
            return True
        
       
        first_head = head
        second_head = head
        
        while(second_head.next != None and second_head.next.next != None):
            first_head = first_head.next
            second_head = second_head.next.next
  
       
        reverse_head = self.reverseList(first_head)     
        
        
        while(reverse_head != None and head != None):
            print(reverse_head.val)
            print(head.val)
            if(reverse_head.val != head.val):
                return False
            reverse_head = reverse_head.next
            head = head.next
        
        return True
  
