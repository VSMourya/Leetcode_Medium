
def oddEvenList(head):


# time - O(n)
# space - O(n)
    if not head:
        return None

    lsOdd = []
    lsEven = []
    dummyHead = head

    while head:
        print(head.val)
        lsOdd.append(head)
        if head.next:
            head = head.next.next
        else:
            head = head.next

    if dummyHead.next:
        dummyHead = dummyHead.next
    else:
        return lsOdd[0]

    while dummyHead:
        lsEven.append(dummyHead)
        if dummyHead.next:
            dummyHead = dummyHead.next.next
        else:
            dummyHead = dummyHead.next

    for i in range(1 ,len(lsOdd)):
        lsOdd[ i -1].next = lsOdd[i]


    lsOdd[-1].next = lsEven[0]

    for i in range(1 ,len(lsEven)):
        lsEven[ i -1].next = lsEven[i]
    lsEven[-1].next = None

    return lsOdd[0]


# ----------------------------------------------------------------------------------


# time - O(n)
# space - O(1)

def oddEvenList(head):

    if not head:
        return
    if not head.next:
        return head

    first = head
    second = head.next
    storedValue = head.next

    dummy = head
    i = 0
    while dummy:
        dummy = dummy.next
        i += 1

    if i % 2 == 0:

        while second.next:
            first.next = first.next.next
            second.next = second.next.next
            first = first.next
            second = second.next

        second.next = None
        first.next = storedValue

        return head
    else:
        while first.next:
            first.next = first.next.next
            second.next = second.next.next
            first = first.next
            second = second.next
        first.next = storedValue
        return head








































