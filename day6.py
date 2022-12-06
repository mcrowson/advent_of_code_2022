from aocd import data
from collections import defaultdict


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
            buffer = msg[end - msg_len:end] 
    
    return end

print("Decreasing Buffer: ")
print(decreasing_buffer(data, 4))
print(decreasing_buffer(data, 14))


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

    print("Time with Sets: ", w_sets)
    print("Time with Pointer: ", w_pointer)
    print("Time with Decreasing Buffer: ", w_decreasing_buffer)


"""
Using Set: 
1909
3380
Using Pointer: 
1909
3380
Time with Sets:  0.40100679197348654
Time with Pointer:  0.5636653330293484
"""
