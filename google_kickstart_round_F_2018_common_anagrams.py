"""
1. find all contiguous substring from given array
2. see if there is anything matched anagram array
"""

class Solution(object):
    ###########################################################
    # find all subset
    ###########################################################
    def findallsubset(self, arr):
        result = []
        if arr == []:
            result.append([])
            return result
        ret = self.findallsubset(arr[1:])
        for n in ret:
            result.append([arr[0]] + n) 
        return result + ret

    def get_findallsubset(self, arr):
        allsubset = self.findallsubset(arr)
        allsubset.pop()
        print(allsubset)
        return allsubset

    ###########################################################
    # find all contiguous subset
    ###########################################################
    def findallsubset_contiguous(self, arr):
        tmp = []
        j = 1
        while j <= len(arr):
            for i in range(0, len(arr)):
                if i+j <= len(arr):
                    tmp.append(arr[i:i+j])
                    # print("arr[{}:{}]={}".format(i, i+j, arr[i:i+j]))
            j += 1
        return tmp
    
    def get_all_contiguous_subset(self, arr1, arr2):
        cnt = 0
        arr1 = [x for x in arr1[:-1]]
        arr2 = [y for y in arr2[:-1]]
        a = self.findallsubset_contiguous(arr1)
        b = self.findallsubset_contiguous(arr2)
        for x in a:
            for y in b:
                if len(y) == len(x) and self.isAnagram(x,y):
                    cnt += 1
                    break
        return cnt

    ###########################################################
    # find all contiguous subset
    ###########################################################
    def array_to_string(self, arr):
        s = ""
        for i in arr:
            s += i
        return s

    def isAnagram(self, a, b):
        tmp = {}
        for x in a:
            if x not in tmp:
                tmp[x] = 1
            else:
                tmp[x] += 1
        for y in b:
            if y not in tmp:
                tmp[y] = 1
            else:
                tmp[y] -= 1
        
        for z in tmp.values():
            if z != 0:
                return False
        return True

# print(Solution().get_all_contiguous_subset("ABB", "BAB"))
# print(Solution().get_all_contiguous_subset("BAB", "ABB"))
# print(Solution().get_all_contiguous_subset("CATYYY", "XXXTAC"))
# print(Solution().get_all_contiguous_subset("SUBXXXXXX", "SUBBUSUSB"))
# print(Solution().get_all_contiguous_subset("AAAA", "AAAA"))
# print(Solution().get_all_contiguous_subset("PLEASEHELPIMTRAPPED", "INAKICKSTARTFACTORY"))

if __name__ == '__main__':
    # print("google_kickstart_round_F_2018_common_anagrams.py")
    # print("input number of total test case: ")
    # num_of_input = int(input())
    # for i in range(1, num_of_input+1):
    #     length_of_string_input = input()
    #     arr1 = str(input())
    #     arr2 = str(input())
    #     print("Case #{}: {}".format(i,Solution().get_all_contiguous_subset(arr1, arr2)))
    
    fw = open("google_kickstart_round_F_2018_common_anagrams_large_Fred.txt", "w")
    with open("A-large-practice.in", 'r') as f:
        line = f.readline()
        num_of_input = int(line)
        i = 1
        while line and i <= num_of_input:
            length_of_string_input = f.readline()
            # print("length_of_string_input ", length_of_string_input)
            arr1 = f.readline()
            # print("arr1 ", arr1)
            arr2 = f.readline()
            # print("arr2 ", arr2)
            # print("Case #{}: {}".format(i,Solution().get_all_contiguous_subset(arr1, arr2)))
            fw.write("Case #{}: {}\n".format(i,Solution().get_all_contiguous_subset(arr1, arr2)))
            print(i)
            i += 1
            
            

    
