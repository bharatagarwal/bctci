"""
# Most prolific level

Given the root of a binary tree, return the most prolific level. 

The prolificness of a level is the average number of children over all the nodes in that level. 

Return -1 if the tree is empty.

Example:

Input:
      O
     /
    O
   / \
  O   O
 / \   \
O   O   O

Output: 1
- Level 0 has prolificness 1
- Level 1 has prolificness 2
- Level 2 has prolificness 1.5
- Level 3 has prolificness 0
The most prolific level is 1, with a prolificness of 2.


for every level,
I want the:
    - number of elements
    - number of children

Constraints:

- The number of nodes is at most 10^5
- The value at each node doesn't matter.
"""

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def process(record):
    most_prolific = tuple()
    max_prolificness = 0

    for level, details in record.items():
        prolificness = details["children"] / details["members"]

        if prolificness > max_prolificness:
            max_prolificness = prolificness
            most_prolific = (level, prolificness)

    return most_prolific


def most_prolific_level(root):
    record = dict()
    q = deque()

    q.append((root, 0))

    while q:
        current, level = q.popleft()

        if not current:
            continue

        if level not in record:
            record[level] = {"members": 1, "children": 0}
        else:
            record[level]["members"] += 1

        if current.left:
            record[level]["children"] += 1
            q.append((current.left, level + 1))
        if current.right:
            record[level]["children"] += 1
            q.append((current.right, level + 1))

    return process(record)


root = Node(
    0, Node(0, Node(0, Node(0), Node(0)), Node(0, None, Node(0))), None
)

print(most_prolific_level(root))
