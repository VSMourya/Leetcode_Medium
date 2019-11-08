


# Time to type a string

alphs = list("abcdefghijklmonpqrstuvxxyz")
maps = {char:i for i,char in enumerate(alphs)}
inp = "cbad"

start = 0
result = 0

for i in inp:
    result += abs(maps[i]-start)
    start = maps[i]

print(result)

