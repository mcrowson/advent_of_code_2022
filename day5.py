from aocd import data
from string import ascii_uppercase
import re
import copy

state, instructions = data.split("\n\n")
heaps = {r: list() for r in state.split("\n")[-1].replace(" ", "")}
boxes = state.split("\n")[:-1]
for row in boxes:
    for col, box in enumerate(row):
        if box not in ascii_uppercase:
            continue
        stack = col // 4
        heaps[str(stack + 1)].insert(0, box)

a_heaps = heaps
b_heaps = copy.deepcopy(heaps)


for inst in instructions.split("\n"):
    match = re.match(r"move (\d+) from (\d+) to (\d+)", inst)
    cnt, src, dst = match.groups()
    cnt = int(cnt)
    for _ in range(cnt):
        a_heaps[dst].append(a_heaps[src].pop())
    b_heaps[dst] += b_heaps[src][-cnt:]
    b_heaps[src] = b_heaps[src][:-cnt]


def get_top(inp):
    return "".join([inp[str(i)][-1] for i in range(1, len(inp) + 1)])


print(get_top(a_heaps))
print(get_top(b_heaps))
