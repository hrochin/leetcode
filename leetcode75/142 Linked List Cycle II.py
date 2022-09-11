# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # How to determine if a node has been visited
        # Keep an array of each node visited. If node.next in array, return node.next
        visitedNodes = []
        while(head):
            if(head.next in visitedNodes):
                return head.next
            else:
                visitedNodes.append(head)
                head = head.next
        return None