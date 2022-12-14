from aocd import data
from itertools import zip_longest
import json

ddata = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

def ensure_list(a):
    if isinstance(a, list):
        return a
    return [a]

def recursive_compare(a, b):
    for ai, bi in zip_longest(a, b, fillvalue=None):
        if isinstance(ai, int) and isinstance(bi, int):
            return bi < ai
        
        elif isinstance(ai, list) and isinstance(bi, list):
            if not recursive_compare(ai, bi):
                return False
        
        elif ai is None:
            continue
        elif bi is None:
            return False
        
        elif not isinstance(bi, list):
            if not recursive_compare(ai[:1], [bi]):
                return False
            
        elif not isinstance(ai, list):
            if not recursive_compare([ai], bi):
                return False    
        
    return True

ordered = []
for i, d in enumerate(data.split('\n\n')):
    a, b = map(json.loads, d.split('\n'))
    if recursive_compare(a, b):
        ordered.append(i + 1)
        
print(ordered)
print(sum(ordered))