
# merge two sorted arrays in O(m+n) time


def merge(a,b):

    ls = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(a) and ptr2 < len(b):

        if a[ptr1] < b[ptr2]:
            ls.append(a[ptr1])
            ptr1+=1
        elif a[ptr1] > b[ptr2]:
            ls.append(b[ptr2])
            ptr2 += 1
        else:
            ls.append(a[ptr1])
            ls.append(b[ptr2])
            ptr1+=1
            ptr2+=1

    minLs = min(a,b,key=lambda x:len(x))
    maxLs = max(a,b,key=lambda x:len(x))

    return ls + maxLs[len(minLs)-1:]


a = [1,3,5,7,9]
b = [0,2,4]

print(merge(a,b))










