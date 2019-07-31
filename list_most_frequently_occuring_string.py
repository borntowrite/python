import re
from collections import Counter

def frequent(string):
    words = {}
    s = string.split()
    for word in s:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    print(sorted(words.items(), key=lambda x: x[1], reverse=True)[0])

s1 = "i am happy but do you happy"
frequent(s1)

def frequent2():
    with open('fred.txt') as f:
        passage = f.read()

    words = re.findall(r'\w+', passage) #cut by word
    words = [word for word in words] #make array
    word_counts = Counter(words).most_common(5)
    print(word_counts)

frequent2()

