
##############################################
##Output the integer number indicating the total number of
##occurrences of the substring in the original string.
##############################################

def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i:len(sub_string)+i] == sub_string:
            count+=1
    return count

print(count_substring('ABCDCDC', 'CDC'))
   
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)
