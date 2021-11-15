#!/bin/python3
# https://www.hackerrank.com/challenges/components-in-graph/ #

import os


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


# List is not hashable, no @cache :(
def find_set(root: int, arr: list[int]) -> int:
    if arr[root] == root: return root
    return find_set(root=arr[root], arr=arr)


def componentsInGraph(gb):
    n: int = len(gb)
    nodes: int = 2 * n + 1
    root: list[int] = [0] * nodes
    count: list[int] = [0] * nodes
    
    for i in range(1, nodes):
        root[i], count[i] = i, 1
    
    for q in gb:
        a, b = find_set(q[0], root), find_set(q[1], root)
        if a == b: continue
        
        root[b] = a
        count[a] += count[b]
        count[b] = 0
    
    mi, ma = nodes, -1
    for i in range(1, nodes):
        if count[i] > 1:
            mi = min(mi, count[i])
        ma = max(ma, count[i])
    return [mi, ma]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()