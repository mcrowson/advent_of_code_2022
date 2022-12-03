from aocd import data
from string import ascii_letters


both = []
for sack in data.split("\n"):
    l = len(sack) // 2
    one, two = sack[:l], sack[l:]
    both += list(set(one).intersection(set(two)))

weights = {l: i + 1 for i, l in enumerate(ascii_letters)}
a = sum([weights[l] for l in both])

print(a)


def gimme_three(lst):
    for i in range(0, len(lst), 3):
        yield lst[i : i + 3]


badges = []
for group in gimme_three(data.split("\n")):
    badges.append(set.intersection(*[set(s) for s in group]).pop())

b = sum([weights[l] for l in badges])
print(b)
