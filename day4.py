from aocd import data

a, b = 0, 0
for pair in data.split("\n"):
    fl, fh, sl, sh = map(int, pair.replace("-", ",").split(","))
    if (fl <= sl and sh <= fh) or (sl <= fl and fh <= sh):
        a += 1
    if range(max(fl, sl), min(fh, sh) + 1):
        b += 1

print(a, b)
