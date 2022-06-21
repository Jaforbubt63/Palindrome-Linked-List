# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle_node(self, head):
        p1, p2 = head, head
        prev = None
        
        while p1 and p2 and p2.next:
            prev = p1
            p1,p2 = p1.next, p2.next.next
            
        prev.next = None
        return p1
    def revers_linked_list(self,head):
        node = head
        prev = None
        next_none = node.next
        
        while node:
            node.next = prev
            prev = node
            node = next_node
            if node:
                next_node = node.next
                
        return prev
    
    def is_palindrome(self, h1, h2):
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1, h2 = h1.next, h2.next
            
        return True
    
        
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        node = self.find_middle_node(head)
        rev_head = self.reverse_linked_list(node)
        
        return self.is_palindrome(head, rev_head)
        