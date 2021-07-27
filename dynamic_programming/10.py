# Assembly Line SchedulingProblem

def min_time(arr, t, e, x):
    
    arr[0][0] += e[0] # adding the entry time for assembly line 1
    arr[1][0] += e[1] # adding the entry time for assembly line 2

    num_stations = len(arr[0])

    for i in range(1, num_stations):
        # for the first assembly line
        arr[0][i] = min(arr[0][i] + arr[0][i -1], arr[0][i] + arr[1][i -1] + t[1][i])

        # for the second assembly line
        arr[1][i] = min( arr[1][i] + arr[1][i -1], arr[1][i] + arr[0][i -1] + t[0][i])
    
    return min(arr[0][num_stations - 1] + x[0], arr[1][num_stations - 1] + x[1])

a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]

print(min_time(a, t, e, x))
    
