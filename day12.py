from aocd import data
from typing import List
from string import ascii_lowercase

letter_i = {l: i for i, l in enumerate(ascii_lowercase)}
letter_i.update({"S": -1, "E": 26})
data_numeric = [[letter_i[i] for i in row] for row in data.split("\n")]


def bfs(dn: List, start: int, end: int) -> int:
    q = [(i, j) for i in range(len(dn)) for j in range(len(dn[0])) if dn[i][j] == start]
    visited = set()
    movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    steps = 0

    while q:
        for _ in range(len(q)):
            spot = q.pop(0)
            visited.add(spot)
            elev = dn[spot[0]][spot[1]]

            if elev == end:
                return steps

            for m in movement:
                possible = (spot[0] + m[0], spot[1] + m[1])
                if (
                    -1 in possible
                    or possible[0] > len(dn) - 1
                    or possible[1] > len(dn[0]) - 1
                ):
                    continue
                if possible in visited or possible in q:
                    continue
                pos_elev = dn[possible[0]][possible[1]]
                if pos_elev > 1 + elev:
                    continue
                q.append(possible)
        steps += 1


print(bfs(data_numeric, -1, 26))
print(bfs(data_numeric, 0, 26))
