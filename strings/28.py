# Second most repeated string in a sequence 

class Solution:
    def secFrequent(self, arr, n):
        count = {}
        for i in range(len(arr)):
            if arr[i] not in count:
                count[arr[i]] = 1
            else:
                count[arr[i]] += 1

        # to find the max just use the max_1 varaible to find the most repeated

        max_1 =  -1 # stores the max
        max_2 = -1 # stores the second max
        for string in arr:
            if count[string] > max_1:
                max_2 = max_1
                max_1 = count[string]
            elif count[string] > max_2 and count[string] != max_1 :
                max_2 = count[string]
        
        for string in arr:
            if count[string] == max_2:
                return string