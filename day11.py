from aocd import data
from operator import mul, add
from math import lcm
import heapq


class Monkey:
    def __init__(
        self,
        worry_items: str,
        operator: str,
        test: str,
        test_true: str,
        test_false: str,
    ) -> None:
        self.worry_items = list(map(int, worry_items.split(": ")[1].split(", ")))
        _, op = operator.split(" = ")
        self.mod = op.split(" ")[-1]
        self.operator = add if " + " in op else mul
        self.test = int(test.split(" ")[-1])
        self.test_true = int(test_true.split(" ")[-1])
        self.test_false = int(test_false.split(" ")[-1])
        self.inspected = 0

    def inspect(self) -> None:
        while self.worry_items:
            item = self.worry_items.pop(0)
            self.inspected += 1
            v = int(self.mod) if self.mod != "old" else item
            v = self.operator(item, v)
            if worry_lcm:
                v %= worry_lcm
            else:
                v = v // 3
            target = self.test_true if v % self.test == 0 else self.test_false
            monkeys[target].worry_items.append(v)


def puzzle(rounds):
    [[m.inspect() for m in monkeys] for _ in range(rounds)]
    monkey_activity = [m.inspected for m in monkeys]
    return mul(*heapq.nlargest(2, monkey_activity))


monkeys = [Monkey(*m.split("\n")[1:]) for m in data.split("\n\n")]
worry_lcm = None
print(puzzle(20))
worry_lcm = lcm(*[m.test for m in monkeys])
print(puzzle(10000))
