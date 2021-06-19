def get_lps(string):
    n = len(string)
    lps = [None]*n

    lps[0] = 0
    l = 0
    i = 1
    while i < n:
        if string[l] == string[i]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l -1]
            else:
                lps[i] = 0
                i += 1
    return lps


def add_to_make_palindrome(string):
    rev_str = string[::-1]
    concat = string + '$' + rev_str
    # getting lps value
    lps = get_lps(concat)
    length = len(string)
    return length - lps[-1]

string = input("Enter the string : ")
print(add_to_make_palindrome(string))
