# Recursively remove all adjacent duplicates
# question => https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def remove_recur(string, last_word):
    if len(string) == 0 or len(string) == 1:
        return string
    
    if string[0] == string[1]:
        last_word = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]

        return remove_recur(string, last_word)

    # ignoring the first charactere
    rem_str = remove_recur(string[1:], last_word)

    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_word = ord(string[0])
        return rem_str[1:]
    if len(rem_str) == 0 and last_word == ord(string[0]):
        return rem_str
    
    return [string[0]] + rem_str


def remove_duplicate(string):
    last_word = 0
    string = list(string)
    ans = remove_recur(string, last_word)
    return ''.join(ans)
    

