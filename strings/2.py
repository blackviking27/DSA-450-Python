# Find Duplicate characters in a string

string = input("Enter the string : ")

def duplicates(string):
    count = {}
    n = len(string)
    for i in range(n):
        if string[i] not in count:
            count[string[i]] = 1
        else:
            count[string[i]] += 1
    
    for i in count:
        if count[i] > 1:
            print(i + " : " + str(count[i]))

duplicates(string)