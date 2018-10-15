def split_and_join(line: str):
    # write your code here
    s = ""
    l = []
    for words in line.split():
    	l.append(words)
    return "-".join(l)

print(split_and_join("i have a kid"))