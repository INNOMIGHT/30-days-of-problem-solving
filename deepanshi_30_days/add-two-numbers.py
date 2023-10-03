class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
    
def addTwoNumbers( l1, l2):
       
        tempHead = ListNode(0)
        ptr3 = tempHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val  = l1.val if l1 is not None else 0
            l2_val = l2.val  if l2 is  not None else 0

            sum = l1_val + l2_val + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            ptr3.next = newNode
            ptr3 = ptr3.next

            l1 = l1.next  if l1 is not None else None
            l2 = l2.next if l2 is not None else None


        result = tempHead.next
        tempHead.next = None
        return result