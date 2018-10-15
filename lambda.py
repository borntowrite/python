
# lambda is anonymous function so it does not have name but
# you can assign it to one variable and call to use 
y = lambda x: x*3 +1
print(y(2))

# combine first name and last name into a single "full name"
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("young", "lee"))

s = "melong          "
print(s.strip()) # strip() will remove all black 
print(s.strip().title()) # title() will make first letter upper case

# lambda argument: return value 

scifi_authors = ["Issac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke",
                 "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
help(scifi_authors.sort)

# sort by first name which is second or word in the end of the string -- [-1] means the last word.
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
scifi_authors.sort(key=lambda name: name.split(" ")[-1].upper())
print(scifi_authors)
scifi_authors.sort(key=lambda name: name.split(" ")[-1], reverse=True)
print(scifi_authors)
print(scifi_authors[0].split(" ")[-1])

def build_func(a,b,c):
    """ return the function f(x) = ax^2 + b*x + c"""
    return lambda x: a*x**2 + b*x + c

f = build_func(2,3,-5)
print(f(0))
print(f(1))
print(f(2))
print(build_func(3,0,1)(2)) # this is same as f(2)


