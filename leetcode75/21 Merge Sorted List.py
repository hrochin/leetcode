# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursiveMerge(list1: Optional[ListNode], list2: Optional[ListNode]):
            # Traverse throw both lists while either pointers are not null

            # Base cases, null values
            if(list1 == None and list2 == None):
                return None
            # If either list is empty, return what remains for the other list
            elif(list1 == None):
                return list2
            elif(list2 == None):
                return list1
            else:
                result_list = ListNode()
                # Check for smaller value with priority to list 1
                if(list1.val <= list2.val):
                    result_list.val = list1.val
                    result_list.next = recursiveMerge(list1.next,list2)
                    
                else:
                    result_list.val = list2.val
                    result_list.next = recursiveMerge(list1,list2.next)

            return result_list
        
        return recursiveMerge(list1, list2)
                