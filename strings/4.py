# Write a Code to check whether one string is a rotation of another

def areRotated(str1, str2):
    if len(str1) != len(str2):
        return False

    # joining the same string
    temp = str1 + str1
    if temp.count(str2) > 0:
        return True
    else:
        return False


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if areRotated(str1, str2):
    print("Rotated")
else:
    print("Not Rotated")