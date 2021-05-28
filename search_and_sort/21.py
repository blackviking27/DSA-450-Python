# Aggressive cows

t = int(input("No. of test cases : "))
for _ in range(t):
    n,c = [int(x) for x in input("Enter n, c : ").split()]
    arr = [] # stalls position
    for i in range(n):
        arr.append(int(input("Enter the stall position : ")))
    
    lb = 0
    un = 10 ** 9
    arr.sort()
    ans = 0
    while lb <= ub:
        mid = (lb + ub) // 2
        cow = 1
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - prev >= mid: # checking if the stall position - previous poistion is greater or equal to mid value
                prev = arr[i]
                cow += 1
                if cow == c:
                    break
        if cow == c:
            ans = mid
            lb = mid + 1
        else:
            ub = mid - 1
    print(ans)
        