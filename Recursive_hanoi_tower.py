
# source, buffer, destination

def TH(n , s, a, d):
        if n == 1:
                print("Move disk 1 from",s,"to",d)
                return
        TH(n-1, s, d, a)
        print("Move disk",n,"from",s,"to",d)
        TH(n-1, a, s, d)

TH(4, 'A', 'B', 'C')



##def hanoi(n, a, b, c):
##        print(a, b, c)
##        if n > 0:
##                # move tower of size n - 1 to helper:
##                hanoi(n - 1, a, c, b)
##                # move disk from source peg to target peg
##                if a: target.append(a.pop())
##                # move tower of size n-1 from helper to target
##                hanoi(n - 1, b, a, c)
##        
##source = [4,3,2,1]
##target = []
##helper = []
##hanoi(len(source),source,helper,target)
