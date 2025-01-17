# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3=[]
        x=0
        i=0
        j=0
        def listtolistnode(list):
            head=ListNode()
            if not list:
                return head
            head=ListNode(list[0])
            current=head
            for x in list[1:]:
                current.next=ListNode(x)
                current=current.next
            return head

        def listnode_to_list(head):
            result=[]
            while(head):
                result.append(head.val)
                head=head.next
            return result
        list_1=listnode_to_list(list1)
        list_2=listnode_to_list(list2)
        while(x is not (len(list_1)+len(list_2))):
            if i == len(list_1):
                while j is not len(list_2):
                    list3.append(list_2[j])
                    x+=1
                    j+=1
                return listtolistnode(list3)
            if j == len(list_2):
                while i is not len(list_1):
                    list3.append(list_1[i])
                    x+=1
                    i+=1
                return listtolistnode(list3)
            if list_1[i] < list_2[j]:
                list3.append(list_1[i])
                x+=1
                i+=1
            else:
                list3.append(list_2[j])
                x+=1
                j+=1



#                           How it was supposed to go like
# 
# 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         temp1 = list1
#         temp2 = list2

#         if not temp1 and not temp2:
#             return None
#         elif not temp1:
#             output = temp2
#             temp2 = temp2.next
#         elif not temp2:
#             output = temp1
#             temp1 = temp1.next
#         elif temp1.val < temp2.val:
#             output = temp1
#             temp1 = temp1.next
#         else:
#             output = temp2
#             temp2 = temp2.next

#         tempOut = output
#         while temp1 or temp2:
#             if not temp1:
#                 tempOut.next = temp2
#                 temp2 = temp2.next
#             elif not temp2:
#                 tempOut.next = temp1
#                 temp1 = temp1.next
#             elif temp1.val < temp2.val:
#                 tempOut.next = temp1
#                 temp1 = temp1.next
#             else:
#                 tempOut.next = temp2
#                 temp2 = temp2.next
#             tempOut = tempOut.next

#         return output