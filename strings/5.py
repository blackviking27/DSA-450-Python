# Write a Program to check whether a string is a valid shuffle of two strings or not

def shuffled(str1, str2, res):
    i = j = k = 0
    l1 = len(str1) # Length of the sub string 1
    l2 = len(str2) # length of the sub string 2
    lr = len(res) # length of the result string

    # total length of string is greater than the length of both sub strings
    if l1 + l2 < lr: return False

    while k < lr:
        if i < l1 and str1[i] == res[k]: i += 1
        elif j < l2 and str2[j] == res[k]: j += 1
        else:
            # the ordered changed or some new character is there
            return False
        k += 1
    
    # If we did not traverse the complete substrings
    if i < l1 or j < l2:
        return False
    else:
        return True

str1, str2 = [str(x) for x in input("Enter s1 and s2 : ").split()]
string = input("Enter the string : ")
if shuffled(str1, str2, string):
    print("Yes")
else:
    print("No")