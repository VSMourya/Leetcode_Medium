

string = "eebbcdddddaa"
arr = [0]*26

for i in string:
    arr[ord(i)-97] +=1

print(arr)
output = ""

i = 0

while i < len(arr):
    if max(arr) == 0:
        break
    elif arr[i] == max(arr):
        output += chr(97+i) + str(arr[i])
        arr[i] = 0
        i = 0
        continue
    i+=1

print(output)

