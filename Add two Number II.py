


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1,l2):


    # time - O(m+n)
    # space - O(m+n)

    a = ""
    b = ""

    while l1:
        a += str(l1.val)
        l1 = l1.next

    while l2:
        b += str(l2.val)
        l2 = l2.next

    c = str(int(a) + int(b))
    lls = [ListNode(int(c[i])) for i in range(len(c))]

    for i in range(1, len(lls)):
        lls[i - 1].next = lls[i]

    lls[-1].next = None

    return lls[0]
