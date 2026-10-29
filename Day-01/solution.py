
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
funds = [0] + list(map(int, input().split()))

edges = []
for _ in range(m):
    u, v, h = map(int, input().split())
    edges.append((h, u, v))

edges.sort()

# DSU
dsu = list(range(n + 1))
dsu_size = [1] * (n + 1)

def find(x):
    while dsu[x] != x:
        dsu[x] = dsu[dsu[x]]
        x = dsu[x]
    return x

# Kruskal Reconstruction Tree
max_nodes = 2 * n + 5
left = [0] * max_nodes
right = [0] * max_nodes
parent = [-1] * max_nodes
weight = [0] * max_nodes
leaf_count = [0] * max_nodes
tree_node = list(range(n + 1))

for i in range(1, n + 1):
    leaf_count[i] = 1

total_nodes = n

for h, u, v in edges:
    ru = find(u)
    rv = find(v)

    if ru == rv:
        continue

    total_nodes += 1
    z = total_nodes

    left[z] = tree_node[ru]
    right[z] = tree_node[rv]
    parent[left[z]] = z
    parent[right[z]] = z
    weight[z] = h
    leaf_count[z] = leaf_count[left[z]] + leaf_count[right[z]]

    if dsu_size[ru] < dsu_size[rv]:
        ru, rv = rv, ru

    dsu[rv] = ru
    dsu_size[ru] += dsu_size[rv]
    tree_node[ru] = z

# Find roots of the reconstruction forest
roots = []
for i in range(1, n + 1):
    if find(i) == i:
        roots.append(tree_node[i])

# Euler order of the original vertices (leaves)
tin = [0] * (total_nodes + 1)
timer = 0

for root in roots:
    stack = [root]
    while stack:
        node = stack.pop()

        if node <= n:
            timer += 1
            tin[node] = timer
        else:
            stack.append(right[node])
            stack.append(left[node])

# Internal nodes inherit their left child's starting position
for node in range(n + 1, total_nodes + 1):
    tin[node] = tin[left[node]]

# Binary lifting
LOG = total_nodes.bit_length()
up = [parent[:total_nodes + 1]]

for k in range(1, LOG):
    prev = up[-1]
    curr = [-1] * (total_nodes + 1)

    for node in range(1, total_nodes + 1):
        p = prev[node]
        if p != -1:
            curr[node] = prev[p]

    up.append(curr)

# Fenwick tree over original vertices
bit = [0] * (n + 1)

def add(i, delta):
    while i <= n:
        bit[i] += delta
        i += i & -i

def prefix(i):
    result = 0
    while i > 0:
        result += bit[i]
        i -= i & -i
    return result

def range_sum(l, r):
    return prefix(r) - prefix(l - 1)

for i in range(1, n + 1):
    add(tin[i], funds[i])

# Process events in chronological order
answers = []

for _ in range(q):
    t, x, v = map(int, input().split())

    if t == 1:
        delta = v - funds[x]
        funds[x] = v
        add(tin[x], delta)

    else:
        node = x

        for k in range(LOG - 1, -1, -1):
            anc = up[k][node]
            if anc != -1 and weight[anc] <= v:
                node = anc

        l = tin[node]
        r = l + leaf_count[node] - 1

        total_funds = range_sum(l, r)
        count = leaf_count[node]

        answers.append(f"{total_funds} {count}")

print("\n".join(answers))
