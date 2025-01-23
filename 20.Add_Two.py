# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        result = ListNode()
        temp=result
        while(1):
            if not l1 and not l2 :
                break
            else:
                if not l1 and l2 :
                    result.val=(l2.val+carry)%10
                    carry =1 if l2.val+carry >9 else 0
                elif not l2 and l1:
                    result.val=(l1.val+carry)%10
                    carry =1 if l1.val+carry >9 else 0
                elif(l1.val+l2.val +carry <10):
                    result.val=l1.val+carry+l2.val
                    carry=0
                elif(l1.val+l2.val +carry >=10):
                    result.val=(l1.val+carry+l2.val)%10
                    carry=1
            l1=l1.next if l1 else None
            l2=l2.next if l2  else None
            if l1 or l2 or carry:
                result.next = ListNode()
                result = result.next
        if carry:
            result.val = carry
        return temp
