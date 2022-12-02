from aocd import data

import heapq


sum_of_snacks = [sum([int(c) for c in elf.split("\n")]) for elf in data.split("\n\n")]

a = max(sum_of_snacks)
print(a)

heapq.heapify(sum_of_snacks)
b = sum(heapq.nlargest(3, sum_of_snacks))

print(b)
