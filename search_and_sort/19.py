# Kth smallest number again, (Imp. Question)
# Hacker earth

n,q = input().split()

ranges= []

for i in range(n):
    a,b = input("Enter the A, B").split() # Taking A,B
    ranges.append([int(a),int(b)]) # aapending the range endpoints

# Sorting the ranges according to the first element in the range
ranges.sort()

# Merging overlapping ranges
idx  = 0
for i in range(1, len(ranges)):
    if ranges[i - 1][1] > ranges[i][0]:
        ranges[i - 1][1] = max(ranges[i -1][1], ranges[i][1])
    else:
        idx += 1
        ranges[idx] = ranges[i] 

# Searching for the kth smallest number
for i in range(q):
    k = int(input("Enter the k: "))
    ans = 0
    for j in range(idx):
        if abs(ranges[i][1] - ranges[i][0]) + 1 > k:
            ans = ranges[i][0] + k - 1
            break
        else:
            k -= abs(ranges[i][1] - ranges[i][0]) + 1
