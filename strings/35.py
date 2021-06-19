# Print Anagrams Together

from collections import defaultdict

def Anagrams(words,n):
    keys = defaultdict(list) # creating a dict object, which returns empty list when key error is present.
    for word in words:
        temp = word
        # sorting the characters in the word,
        # each anagram will be the same word when sorted thus that can be used as the key
        temp = ''.join(sorted(temp)) 
        keys[temp].append(word)
    ans = [] # storing the answer in this array
    for key in keys:
        ans.append(keys[key])
    return ans
