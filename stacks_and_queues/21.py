# Stack Permutations (Check if an array is stack permutation of other)
from queue import Queue

def checkStackPermutation(in_arr, out_arr):
    
    #inserting elements in in_queue
    in_queue = Queue()
    for el in in_arr:
        in_queue.put(el)
    
    # insert elements in out_queue
    out_queue = Queue()
    for el in out_arr:
        out_queue.put(el)
    
    stack = []

    while not in_queue.empty():
        el = in_queue.get()
        if el == out_queue.queue[0]:
            out_queue.get()
            while len(stack) != 0 and stack[-1] == out_queue.queue[0]:
                stack.pop()
                out_queue.get()
        else:
            stack.append(el)

    return in_queue.empty() and len(stack) == 0

# driver code
input_arr = [1, 2, 3, 4, 5]
output_arr = [5, 4, 3, 2, 1]

print(checkStackPermutation(input_arr, output_arr))

