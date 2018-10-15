##str.isalnum() 
##This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
##str.isalpha() 
##This method checks if all the characters of a string are alphabetical (a-z and A-Z).
##str.isdigit() 
##This method checks if all the characters of a string are digits (0-9).
##str.islower() 
##This method checks if all the characters of a string are lowercase characters (a-z).
##str.isupper() 
##This method checks if all the characters of a string are uppercase characters (A-Z).

def checkstr(s: str):
    res = ""
    isalnum=isalpha=isdigit=islower=isupper = False
    for i in s:
        if i.isalnum():
            isalnum = True
            break

    for i in s:
        if i.isalpha():
            isalpha = True
            break

    for i in s:
        if i.isdigit():
            isdigit = True
            break

    for i in s:
        if i.islower():
            islower = True
            break

    for i in s:
        if i.isupper():
            isupper = True
            break
    
    res = str(isalnum) + "\n" + str(isalpha) + "\n" + str(isdigit) + "\n" + str(islower) + "\n" + str(isupper)
    return res

if __name__ == '__main__':
    s = input()
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in s))
    #print(checkstr(s))




