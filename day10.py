from aocd import data


register, cycle, power = 1, 0, 0
instructions = data.split("\n")
current, nxt = None, None

while instructions or current:
    cycle += 1
    if not current:
        v = instructions.pop(0)
        if v != "noop":
            _, mod = v.split(" ")
            nxt = int(mod)

    if cycle == 20 or (cycle - 20) % 40 == 0:
        power += register * cycle

    if current:
        register += current

    current = nxt
    nxt = None

print(power)
