# word Ladder 

from collections import deque
class Solution:
    def wordLadder(self, beginWord, endWord, wordList):
        # creating a set inorde to perform O(n) solution
        wordList = set(wordList)
        wordLen = len(beginWord)

        # stores the word which are part of the solution 
        q = deque([[beginWord, 1]])

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            # moving through each character of the word
            # and replacing the words and checking if we can find
            # the new word in the wordlist or not
            for i in range(wordLen):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        q.append([new_word, length + 1])
        
        return 0