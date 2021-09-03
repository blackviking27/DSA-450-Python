# Merge Overlapping Intervals

# stack implementation
def mergerIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    # stores the intervals
    stack = [intervals[0]]

    for i in range(1, len(intervals)):
        top = stack.pop()
        if top[1] > intervals[i][0]:
            top[1] = max(top[1], intervals[i][1])
            stack.append(top)
        else:
            stack.append(top)
            stack.append(intervals[i])
    
    return stack

# without stack implementation

def mergerInt(arr):
    arr.sort(key = lambda x: x[0])
    idx = 0
    for i in range(1, len(arr)):
        if arr[idx][1] >= arr[i][0]:
            arr[idx][1] = max(arr[idx][1], arr[i][1])
        else:
            idx += 1
            arr[idx] =  arr[i]
    
    return arr[:idx + 1]
