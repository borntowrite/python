####################################
# toggle char in string
####################################
print(ord('A')) #65
print(ord('Z')) #90
print(ord('a')) #97
print(ord('z')) #122

def togglechar(s: str):
    s2 = ""
    for i in s:
        if i.isupper():
            s2 += i.lower()
        else:
            s2 += i.upper()
    return s2

print(togglechar("Www.HackerRank.com"))