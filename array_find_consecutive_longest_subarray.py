#########################################
# find longest consecutive subarray in given array
# don't need to be sorted array
# it'll just iterate thru from the beginning
# for example, arr[0] = 4 (i-1) does not have 3 in given array
# execute below code and if there is 5, and 6, then it'll increase
# the length (while). 
# if not, it'll execute 'continue' and begin for loop again
# means there is smaller value in the given array already
#########################################
arr = [4,2,1,6,5]
values = set() # set sorts array - soring takes O(n logn)
def consecutive(arr):
	for i in arr:
		values.add(i)
	#print(values)
	mx = 0
	for i in values:
		if i-1 in values:
			continue
		length = 0
		while i in values:
			length += 1
			i += 1
		mx = max(mx, length)
	return mx

print(consecutive(arr))