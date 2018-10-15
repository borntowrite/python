
###########################################
# Recursive Multiplication
# can't handle larger number - due to limited number of recursive call
###########################################
def multiply(x,y):
 
    # 0 multiplied with anything
    # gives 0 
    if(y == 0):
        return 0
 
    # Add x one by one 
    if(y > 0 ):
        return (x + multiply(x, y - 1))
 
    # The case where y is negative
    if(y < 0 ):
        return -multiply(x, -y)

print(multiply(10,10))
print(multiply(10,-10))