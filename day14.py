from aocd import data
import string

data = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


filled = set()
filled_b = set()

for formation in data.split('\n'):
    points = formation.split(' -> ')
    for i in range(len(points) - 1):
        x, y = points[i].split(','), points[i+1].split(',')
        xs, xe = sorted(map(int, [x[0], y[0]]))
        ys, ye = sorted(map(int, [x[1], y[1]]))
        for xi in range(xs, xe + 1):
            for yi in range(ys, ye + 1):
                filled.add((xi, yi))
                filled_b.add((xi, yi))

print(filled)

sand_added = 0
sand_start = (500, 0)
current_sand = sand_start
lowest_rock = max(r[1] for r in filled)

while True:  # temp sanity
    if current_sand[1] > lowest_rock:
        break
    elif (current_sand[0], current_sand[1] + 1) not in filled:  # go down
        current_sand = (current_sand[0], current_sand[1] + 1)
        continue
    elif (current_sand[0] - 1, current_sand[1] + 1) not in filled:
        current_sand = (current_sand[0] - 1, current_sand[1] + 1)
        continue
    elif (current_sand[0] + 1, current_sand[1] + 1) not in filled:
        current_sand = (current_sand[0] + 1, current_sand[1] + 1)
    else:
        filled.add(current_sand)
        current_sand = sand_start
        sand_added += 1

print(sand_added)


# Part b
sand_added = 0
sand_start = (500, 0)
current_sand = sand_start
lowest_rock = max(r[1] for r in filled_b)


while True:  # temp sanity
    if current_sand[1] > lowest_rock + 2:
        filled_b.add(current_sand)
        current_sand = sand_start
        sand_added += 1
    
    elif (current_sand[0], current_sand[1] + 1) not in filled:  # go down
        current_sand = (current_sand[0], current_sand[1] + 1)
        continue
    elif (current_sand[0] - 1, current_sand[1] + 1) not in filled:
        current_sand = (current_sand[0] - 1, current_sand[1] + 1)
        continue
    elif (current_sand[0] + 1, current_sand[1] + 1) not in filled:
        current_sand = (current_sand[0] + 1, current_sand[1] + 1)
    else:
        filled_b.add(current_sand)
        current_sand = sand_start
        sand_added += 1
        if current_sand == sand_start:
            break

print(sand_added)