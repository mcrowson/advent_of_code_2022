from aocd import data
from collections import defaultdict
import heapq


cmd_hist = data.split("\n")

dir_sizes = defaultdict(int)

current_path = []
for cmd in cmd_hist:
    if cmd[:4] == "$ cd":
        if cmd[5:] == "..":
            current_path.pop(-1)
        else:
            current_path.append(cmd[5:])
    elif "$ " != cmd[:2] and "dir " != cmd[:4]:
        fs, _ = cmd.split(" ")
        path = ""
        for dir in current_path:
            path += f"/{dir}"
            dir_sizes[path] += int(fs)


a = sum([s for s in dir_sizes.values() if s <= 100000])
print(a)

desired_space = 70000000 - 30000000
current_space = dir_sizes["//"]
need_to_free = current_space - desired_space

possible_deletions = []

for k, v in dir_sizes.items():
    if v < need_to_free:
        continue
    heapq.heappush(possible_deletions, (v, k))

b = heapq.heappop(possible_deletions)
print(b[0])
