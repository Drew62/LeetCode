# This should be medium difficulty...
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        output = []
        curr = self
        while curr:
            output.append(curr.val)
            curr = curr.next

        return output

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2            
                
def createLinkedList(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

solution = Solution()
list1 = createLinkedList([1,3,5])
list2 = createLinkedList([2,4,6])
solution.mergeTwoLists(list1, list2)
