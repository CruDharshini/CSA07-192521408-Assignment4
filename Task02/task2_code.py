"""Compare topologies and test whether every office remains connected after one link fails."""
from itertools import combinations
from collections import deque

def links(kind, n):
    nodes = list(range(n))
    if kind == "bus":
        return [(i, i + 1) for i in range(n - 1)]
    if kind == "ring":
        return [(i, (i + 1) % n) for i in range(n)]
    if kind == "star":
        return [("hub", i) for i in nodes]
    if kind == "mesh":
        return list(combinations(nodes, 2))
    raise ValueError(kind)

def connected_after_failure(edges, n, broken):
    adjacency = {i: set() for i in range(n)}
    adjacency["hub"] = set()
    for a, b in edges:
        if (a, b) == broken or (b, a) == broken:
            continue
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen.intersection(range(n))) == n

def main():
    n = 6
    for kind in ("bus", "ring", "star", "mesh"):
        e = links(kind, n)
        vertices = set(x for edge in e for x in edge)
        max_ports = max(sum(x in edge for edge in e) for x in vertices)
        survived = sum(connected_after_failure(e, n, broken) for broken in e)
        print(f"{kind:<5} links {len(e):2} max ports on one device {max_ports} "
              f"single-link failures survived {survived}/{len(e)}")
    print("\nGrowth: n=20")
    for kind in ("star", "mesh"):
        print(f"{kind}: {len(links(kind, 20))} links")

if __name__ == "__main__":
    main()
