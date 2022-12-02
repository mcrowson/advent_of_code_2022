from aocd import data

import heapq


sum_of_snacks = [sum([int(c) for c in elf.split("\n")]) for elf in data.split("\n\n")]
heapq.heapify(sum_of_snacks)

a = heapq.nlargest(1, sum_of_snacks)
print(a)

b = sum(heapq.nlargest(3, sum_of_snacks))
print(b)
