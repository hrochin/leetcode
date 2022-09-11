# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new list to push new nodes to
        reversedList = None
        
        # Iterate over list while not null
        while(head != None):
            # Push into new list (Stack)
            reversedList = ListNode(head.val, reversedList)   
            # Move to next item in original list
            head = head.next
            
        return reversedList