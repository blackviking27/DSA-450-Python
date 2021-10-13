# Rearrange characters in a string such that no two adjacent are same

from queue import PriorityQueue as pq

# with out priority queue


def rearrange_1(string):
    n = len(string)

    freq = {}
    for char in string:
        freq[char] = 1 + freq.get(char, 0)

    max_freq = -1
    max_char = ""  # character with max frequency

    for char in freq:
        if freq[char] > max_freq:
            max_freq = freq[char]
            max_char = char

    if max_freq > n - max_freq + 1:
        return ""

    res = [""] * n
    idx = 0
    while max_freq != 0:
        res[idx] = max_char
        max_freq -= 1
        idx += 2

    del freq[max_char]  # removing the max freq character

    for char in freq:
        while freq[char] != 0:
            if idx >= n:
                idx = 1

            res[idx] = char
            freq[char] -= 1
            idx += 2

    return "".join(res)


# priority queue method
def rearrange_2(string):
    n = len(string)

    freq = {}
    for char in string:
        freq[char] = 1 + freq.get(char, 0)

    q = pq()
    # mainting a max heap
    for char in freq:
        q.put([-1 * freq[char], char])

    res = ""
    prev = [1, '#']  # to tell the previous character in the queue
    while not q.empty():
        count, c = q.get()
        res += c

        if prev[0] < 0:
            q.put(prev)

        count += 1
        prev = [count, c]

    return res if n == len(res) else ""
