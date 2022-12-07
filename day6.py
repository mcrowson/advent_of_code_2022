from aocd import data
from collections import defaultdict, deque


def set_it(msg, msg_len):
    for i in range(msg_len, len(msg)):
        if len(set(msg[i - msg_len : i])) == msg_len:
            return i


print("Using Set: ")
print(set_it(data, 4))
print(set_it(data, 14))


def pointer(msg, msg_len):
    end = msg_len
    buffer = msg[:end]
    counts = defaultdict(int)
    for ch in buffer:
        counts[ch] += 1

    while len(counts) != msg_len:
        counts[buffer[0]] -= 1
        if counts[buffer[0]] == 0:
            del counts[buffer[0]]
        counts[msg[end]] += 1
        buffer = buffer[1:] + msg[end]
        end += 1

    return end


print("Using Pointer: ")
print(pointer(data, 4))
print(pointer(data, 14))


def decreasing_buffer(msg, msg_len):
    end = msg_len
    buffer = msg[:end]

    while buffer:
        cmp, buffer = buffer[0], buffer[1:]
        if cmp in buffer:
            end += 1
            buffer = msg[end - msg_len : end]

    return end


print("Decreasing Buffer: ")
print(decreasing_buffer(data, 4))
print(decreasing_buffer(data, 14))


def two_pointers(msg, msg_len):
    beg, end = 0, 1
    buffer = msg[0]
    while end - beg < msg_len:
        nxt = msg[end]
        if nxt not in buffer:
            buffer += nxt
            end += 1

        else:
            beg += 1
            buffer = buffer[1:]

    return end


print("Two Pointers: ")
print(two_pointers(data, 4))
print(two_pointers(data, 14))


def gav_idea(msg: str, window_size: int):
    for i in range(len(msg) - window_size + 1):
        window = msg[i : i + window_size]
        for j in range(1, len(window)):
            window_slice = window[j:]
            if window[j - 1] in window_slice:
                break
            if len(window_slice) == 1:
                return i + window_size
    return None


print("Gav Idea: ")
print(gav_idea(data, 4))
print(gav_idea(data, 14))

# Gav found this one on reddit, timing it
def find_marker(msg, n):
    marker = deque()
    msg_start = 0
    while len(marker) < n:
        current = msg[msg_start]
        msg_start += 1
        while current in marker:
            marker.popleft()
        marker.append(current)
    return msg_start


print("Find Marker: ")
print(find_marker(data, 4))
print(find_marker(data, 14))

if __name__ == "__main__":
    import timeit

    w_sets = timeit.timeit(
        "set_it(data, 4)",
        number=1000,
        setup="from __main__ import set_it; from aocd import data",
    )
    w_pointer = timeit.timeit(
        "pointer(data, 4)",
        number=1000,
        setup="from __main__ import pointer; from aocd import data",
    )
    w_decreasing_buffer = timeit.timeit(
        "decreasing_buffer(data, 4)",
        number=1000,
        setup="from __main__ import decreasing_buffer; from aocd import data",
    )
    w_two_pointers = timeit.timeit(
        "two_pointers(data, 4)",
        number=1000,
        setup="from __main__ import two_pointers; from aocd import data",
    )
    w_gav_idea = timeit.timeit(
        "gav_idea(data, 4)",
        number=1000,
        setup="from __main__ import gav_idea; from aocd import data",
    )
    w_find_marker = timeit.timeit(
        "find_marker(data, 4)",
        number=1000,
        setup="from __main__ import find_marker; from aocd import data",
    )

    print("Time with Sets: ", w_sets)
    print("Time with Pointer: ", w_pointer)
    print("Time with Decreasing Buffer: ", w_decreasing_buffer)
    print("Time with Two Pointers: ", w_two_pointers)
    print("Time with Gav Idea: ", w_gav_idea)
    print("Time with Find Marker: ", w_find_marker)


"""
Time with Sets:  0.4068907499895431
Time with Pointer:  0.5638869579997845
Time with Decreasing Buffer:  0.39821137505350634
Time with Two Pointers:  0.3642351250164211
Time with Gav Idea:  0.6578782919677906
Time with Find Marker:  0.27565645799040794
"""
