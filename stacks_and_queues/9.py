# The celebrity Problem

class Solution:
    def celebrity(self, M, n):
        celeb = 0 

        for i in range(n):
            # if the current celeb knows anybody then they are not the celeb
            if M[celeb][i] == 1:
                celeb = i
        
        # confirming if they are celebrity or not
        for i in range(n):
            # checking for false condition
            # False conditions:
            # if celeb knows somebody or someone does not know the celeb
            if i != celeb and (M[celeb][i] == 1 or M[i][celeb] == 0):
                return -1

        return 1
