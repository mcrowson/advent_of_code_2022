from aocd import data
import pandas as pd
from collections import defaultdict


data = '''30373
25512
65332
33549
35390'''

dn = [[int(s) for s in row] for row in data.split('\n')]
#print(dn)

df = pd.DataFrame(dn)
#print(df)
visible = set()
tree_score = {}

directions = [(1, 1), (1, -1), (-1, -1),(-1, 1)]

for row_i, row in df.iterrows():
    #print(index, row)
    for col_i, tree in row.items():
        loc = (row_i, col_i)
        if loc == (1, 2):
            pass
        left = df.loc[row_i,:col_i-1]
        on_perimiter = (0 in loc) or (loc[0] == df.shape[0] -1 ) or (loc[1] == df.shape[1] -1 )
        look_left = tree > df.loc[row_i,:col_i -1]
        look_right = tree > df.loc[row_i,min([col_i + 1, df.shape[1]]):].max()
        look_up = tree > df.loc[:row_i-1, col_i].max()
        look_down = tree > df.loc[min([row_i + 1, df.shape[0]]):, col_i].max()
        if any([
            on_perimiter,
            look_left,
            look_right,
            look_up,
            look_down
        ]):
            visible.add(loc)
            tree_score[loc] = 1
            if look_up:
                tree_score[loc] *= loc[0]
            if look_left:
                tree_score[loc] *= loc[1]
            if look_right:
                tree_score[loc] *= df.shape[1] - 1 - loc[1]
            if look_down:
                tree_score[loc] *= df.shape[0] - 1 - loc[0]
             

print(visible)
print(len(visible))
        

for dir in directions:
    tallest = -1

