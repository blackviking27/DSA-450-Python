# Permutations of a given string

res = []
def permute(string, ans):
    if len(string) == 0:
        # print(ans, end=" ")
        global res
        res.append(ans)
        return
    
    for i in range(len(string)):
        ch = string[i]
        left_substr = string[0:i]
        right_substr = string[i + 1:]
        rest = left_substr + right_substr
        permute(rest, ans + ch)

string = input("Enter the string : ")
permute(string, "")
print(res)

