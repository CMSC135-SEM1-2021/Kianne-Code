import sys
import math
from collections import defaultdict

def Sever(si, gateways):
    global links
    for i in gateways:
        if i in links[si]:
            return [si, i]
    for j in gateways:
        if len(links[j]) > 0:
            return [j, links[j][0]]
    return [0, 0]

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
gateways = []
links = defaultdict(list)

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links[n1].append(n2)
    links[n2].append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    c1, c2 = Sever(si, gateways)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(c1, c2)
    links[c1].remove(c2)
    links[c2].remove(c1)
