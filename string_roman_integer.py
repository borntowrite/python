############################################################################
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
############################################################################

def int_to_roman(num):
	print(num)
	M = ["", "M", "MM", "MMM"]
	C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
	X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
	I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
	return M[num/1000] + C[(num/100)%10] + X[(num/10)%10] + I[num%10]

print(int_to_roman(1994))

def romanToInt(s):
	
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, \
         'XL':40, 'XC':90, 'CD':400, 'CM':900}
    # Keep a record for all special cases of substraction
    l = []
    num = 0
    j = 0
    
    # Record the index location of all substractions
    for i in range(len(s) - 1):
        if s[i:i+2] in d:
            l.append(i)
            
    # Gradually add up to the corresponding value of the Roman
    while j < len(s):
        if j not in l:
            num += d[s[j]]
            j += 1
        
        else:
            num += d[s[j:j+2]]
            j += 2
            
    return num

print(romanToInt('MCMXCIV'))