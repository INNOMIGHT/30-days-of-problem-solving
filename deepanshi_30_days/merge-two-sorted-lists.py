class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        tempNode = ListNode(0)
        ptr = tempNode
        while list1 is  not  None or list2 is not None:
            if list1 is None:
                ptr.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                ptr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                if list2.val  <  list1.val:
                    ptr.next = ListNode(list2.val)
                    list2 = list2.next
                elif list1.val <=  list2.val:
                    ptr.next = ListNode(list1.val)
                    list1 = list1.next
            ptr = ptr.next
        headNode = tempNode.next
        tempNode.next = None
        return headNode 