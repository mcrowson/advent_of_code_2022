from aocd import data

win, draw, lose = 6, 3, 0

my_move_map = {l: i + 1 for i, l in enumerate(["X", "Y", "Z"])}
their_move_map = {l: i + 1 for i, l in enumerate(["A", "B", "C"])}

a = 0
for round in data.split("\n"):
    them, me = round.split(" ")
    if my_move_map[me] - 1 % 3 == their_move_map[them] % 3:
        a += win + my_move_map[me]
    elif my_move_map[me] == their_move_map[them]:
        a += draw + my_move_map[me]
    else:
        a += lose + my_move_map[me]

print(a)

their_b_move_map = {l: i for i, l in enumerate(["A", "B", "C"])}

b = 0
for round in data.split("\n"):
    them, result = round.split(" ")
    if result == "Z":
        b += (their_b_move_map[them] + 1) % 3 + win + 1
    elif result == "Y":
        b += their_b_move_map[them] + draw + 1
    else:
        b += (their_b_move_map[them] - 1) % 3 + lose + 1

print(b)
