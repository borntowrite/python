
####################################
# SET
####################################
example = set()
print(dir(example))
print(help(example.add))

example.add(42)
example.add(False)
example.add(3.412321)
example.add("melong")
print(example)

print(help(example.remove))

example.remove(42)
print(example)

#example.remove(50) # throw error
example.discard(50) # do nothing 

