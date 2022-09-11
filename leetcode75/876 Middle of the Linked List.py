# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using 2 pointers. One at 1 step per iterationa and the other at 2.
        twoSteps = head
        while(twoSteps != None):
            # Dealing with even and odd lists
            # Odd number of nodes means faster pointer will land on the last node while even will land on the 2nd to last.
            # To get the correct middle node, accounting for the 2nd of the 2 nodes when even.
            if(twoSteps.next == None):
                return head
            elif(twoSteps.next.next == None):
                return head.next
            else:
                twoSteps = twoSteps.next.next
                head = head.next
        return head