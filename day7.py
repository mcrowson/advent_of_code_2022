from aocd import data
from collections import defaultdict
import heapq


cmd_hist = data.split("\n")

dir_sizes = defaultdict(int)

current_path = []
for cmd in cmd_hist:
    pref, suf = cmd[:4], cmd[5:]
    if pref in ("$ ls", "dir "):
        continue
    elif pref == "$ cd":
        if suf == "..":
            current_path.pop(-1)
        else:
            current_path.append(suf)
    else:
        path = ""
        for dir in current_path:
            path += f"/{dir}" if dir != "/" else "/"
            dir_sizes[path] += int(cmd.split(" ")[0])


a = sum([s for s in dir_sizes.values() if s <= 100000])
print(a)

need_to_free = dir_sizes["/"] - (70000000 - 30000000)

possible_deletions = []
[heapq.heappush(possible_deletions, (v, k)) for k, v in dir_sizes.items() if v >= need_to_free]

b = heapq.heappop(possible_deletions)
print(b[0])
