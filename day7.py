from aocd import data
from typing import List

data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''



'''
def get_dir_size(dir_name: str, parent_path: List=None) -> int:
    this_size = 0
    if not parent_path:
        parent_path = []
    contents = []
    
    # scan input for "cd %"
    pos = cmd_hist.index(f'$ cd {dir_name}')
    
    # skip the ls command
    pos += 2
    # get everything up to next $ and that is this dir contents
    line = cmd_hist[pos]
    while line[0] != '$' and pos < len(cmd_hist) - 1:
        print(line)
        contents.append(line)
        pos += 1
        line = cmd_hist[pos]
    
    # First recursively call get_dir_sizes on internal directories
    for c in contents:
        if c[:4] == 'dir ':
            this_size += get_dir_size(c[4:], parent_path + [dir_name])
        else:
            print(c)
            fs, _ = c.split(' ')
            this_size += int(fs)
    
    dir_sizes[dir_name] = this_size
    # save to dir_sizes
    return this_size
    
get_dir_size('/')

print("more")
print(dir_sizes)
'''

cmd_hist = data.split('\n')

dir_sizes = {}

tree = {}

current_path = []
for cmd in cmd_hist:
    if cmd[:4] == '$ cd':
        current_path.append(cmd[:4])
    if cmd == '$ ls':
        


a = sum([s for d, s in dir_sizes.items() if s <= 100000]) 
print(a)   
