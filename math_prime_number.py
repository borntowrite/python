import math

#####################################################
# isPrime - mysql
#####################################################
##SET @num:=1;SET @num2:=1;
##SELECT GROUP_CONCAT(NUMB SEPARATOR '&')
##FROM (
##    SELECT @num:=@num+1 as NUMB FROM
##    information_schema.tables t1,
##    information_schema.tables t2
##    LIMIT 1000
##) a 
##WHERE NOT EXISTS (
##		SELECT * FROM (
##			SELECT @num2:=@num2+1 as NUMA FROM
##			    information_schema.tables t1,
##			    information_schema.tables t2
##			    LIMIT 1000
##		) b WHERE FLOOR(NUMB/NUMA)=(NUMB/NUMA) AND NUMA<NUMB
##)

#####################################################
# isPrime - #2
#####################################################
# Python program for practical application of sqrt() function
# import math module
# function to check if prime or not 
def check(n):
    if n == 1:
        return False
         
        # from 1 to sqrt(n) 
    for x in range(2, (int)(math.sqrt(n))+1):
        if n % x == 0:
            print(n, x)
            return False
    return True
 
# driver code
n = 187
if check(n):
    print("prime") 
else:
    print("not prime")

print(math.sqrt(187))
    
#####################################################
# isPrime - #1
#####################################################
##def isPrime(n):
##    if(n<2): return False
##    elif(n==2): return True
##    elif(n==3): return True
##    elif(n==5): return True
##    elif(n==7): return True
##    elif(n%2==0): return False
##    elif(n%3==0): return False
##    elif(n%5==0): return False
##    elif(n%7==0): return False
##
##    return True
##
##i=0
##for i in range(1000):
##    if isPrime(i):
##        print(i, "------ Prime Number")
##    else:
##        print(i, isPrime(i))

##0 False
##1 False
##2 ------ Prime Number
##3 ------ Prime Number
##4 False
##5 ------ Prime Number
##6 False
##7 ------ Prime Number
##8 False
##9 False
##10 False
##11 ------ Prime Number
##12 False
##13 ------ Prime Number
##14 False
##15 False
##16 False
##17 ------ Prime Number
##18 False
##19 ------ Prime Number

#####################################################
# sqrt
#####################################################
##print(int(math.sqrt(7)))
##print(math.sqrt(7))
