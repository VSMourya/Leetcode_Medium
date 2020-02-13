# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#

def plusOne(head):
    if not head:
        return

    num = ""
    while head:
        num += str(head.val)
        head = head.next

    num = list(str(int(num) + 1))
    ptr = start = ListNode(int(num[0]))

    for i in range(1, len(num)):
        ptr.next = ListNode(int(num[i]))
        ptr = ptr.next

    ptr.next = None

    return start

