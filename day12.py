from aocd import data
from operator import add
from string import ascii_lowercase

data = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

q = []
visited = set()
movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
steps = 0

for i, row in enumerate(data.split('\n')):
    for j, letter in enumerate(row):
        if letter == 'S':
            q.append((i, j))
            
while q:
    for _ in range(len(q)):
        spot = q.pop(0)
        letter = data[spot[0]][spot[1]]
        
        if spot == 'E':
            print(steps)
        
        if letter == 'S':
            spot_elev = -1
        else:
            spot_elev = ascii_lowercase.index(letter)
        for m in movement:
            possible = (spot[0] + m[0])
            if possible in visited:
                continue
            pos_letter = data[possible[0]][possible[1]]
            elev = ascii_lowercase.index(pos_letter)
            if elev + 1 != spot_elev:
                continue
            q.append(possible)
    steps += 1
            
            