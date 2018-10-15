"""
Anagram Solution - #1
"""
def anagram1(s1, s2):
    letters = {}
    # increase count 1 for all char
    for ch in s1.lower():
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
    # decrease count 1 for all char
    for ch in s2.lower():
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] -= 1
    # if any char's count is not 0, then.. 
    for i in letters.values():
        if i != 0: return False
    return True

print(anagram1('ABCDE', 'edcba'))

"""
Anagram Solution - #1
"""
def isanagram2(wrd1, wrd2):
    # create word dic 
    # {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    wrd1_dict = {k: 0 for k in wrd1}
    wrd2_dict = {k: 0 for k in wrd2}
    # increase count of each char
    for c1, c2 in zip(wrd1, wrd2):
        wrd1_dict[c1] += 1
        wrd2_dict[c2] += 1
    # compare two dic and see if it's same or not
    if wrd1_dict == wrd2_dict:
        return True
    return False

print(isanagram2('ABCDE', 'edcba')) # there is no lower case check hence it's false.

