# Print all Subsequences of a string.

res = []

def subsequence(string, ans):
    if len(string) == 0:
        # you can print directly too
        # print(ans, end=" ")
        global res # appending the answer to the global res
        res.append(ans)
        return
    
    #including the current element in the answer
    subsequence(string[1:], ans + string[0])

    # not including the current element in answer
    subsequence(string[1:], ans)

string = input("Enter the string : ")
subsequence(string, "")
print(res)

