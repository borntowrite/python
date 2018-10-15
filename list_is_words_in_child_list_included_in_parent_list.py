#############################################################
#is words in child list included in parent list?- Hackerrank
#############################################################
mn = input().split
m = int(mn[0])
n = int(mn[1])
magazine = input().rstrip().split()
ransom = input().rstrip().split()
m=6
n=4
magazine=['give', 'me', 'one', 'grand' ,'today', 'night']
ransom=['give', 'one', 'grand' ,'today']
e=OrderedDict()
isransom=True
for j in magazine:
    e.update({j : 0})
for j in magazine:
    e[j] += 1
for j in ransom:
    e[j] -= 1
for j in ransom:
    if e[j] < 0:
        isransom=False
if isransom:
    print("Yes")
else:
    print("No")
