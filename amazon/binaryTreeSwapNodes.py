import os
from typing import List, Optional

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def swap(root: Node, k: int):
    def swp(n: Optional[Node], k: int, cur: int):
        if not n:
            return
        
        if cur % k == 0:
            n.left, n.right = n.right, n.left

        swp(n.left, k, cur+1)
        swp(n.right, k, cur+1)

    swp(root, k, 1)

def listToTree(indexes: List[List[int]]) -> Optional[Node]:
    nodes = [Node(i+1) for i in range(len(indexes))]
    for i, row in enumerate(indexes):
        n = nodes[i]
        n.left = nodes[row[0]-1] if row[0] > 0 else None
        n.right = nodes[row[1]-1] if row[1] > 0 else None
    return nodes[0]

def inOrder(root: Node) -> List[int]:
    rs = []
    def recurse(n: Optional[Node]):
        if not n:
            return
        recurse(n.left)
        rs.append(n.val)
        recurse(n.right)
    
    recurse(root)
    return rs

def swapNodes(indexes: List[List[int]], queries: List[int]) -> List[List[int]]:
    root = listToTree(indexes)
    if not root:
        return []

    rs = []
    for k in queries:
        swap(root, k)
        rs.append(inOrder(root))

    return rs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

