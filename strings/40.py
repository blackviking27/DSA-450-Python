# Transform One String to Another using Minimum Number of Given Operation

def operations(s1, s2):
    n = len(s1)
    m = len(s2)

    # different lengths cannot be converted
    if n!= m: return -1

    count = [0] * 256

    for i in range(n):
        count[ord(s2[i])] += 1
    for i in range(n):
        count[ord(s1[i])] -= 1
    
    # count of all should be zero since all the characters were accounted for by both the strings
    for i in range(256):
        if count[i]: # since 0 means false, the code inside 'if' will not run
            return -1
    
    res = 0
    i = n -1
    j = n - 1
    while i >= 0:
        while i >= 0 and s1[i] != s2[j]:
                i -= 1
                res += 1
        if i >= 0:
            i -= 1
            j -=1
    return res

print(operations("EACBD", "EABCD"))