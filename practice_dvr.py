INF = 999
cost = []
n = int(input("Enter number of routers: "))
for _ in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

dist = [row[:] for row in cost]
nexthop = [[-1]*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
    for j in range(n):
        if i != j and cost[i][j] != INF:
            nexthop[i][j] = j
        elif i == j:
            nexthop[i][j] = i

updated = True
while updated:
    updated = False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cost[i][k] != INF and dist[k][j] != INF:
                    newcost = cost[i][k] + dist[k][j]
                    if newcost < dist[i][j]:
                        dist[i][j] = newcost
                        nexthop[i][j] = k
                        updated = True

for i in range(n):
    print(f"Router {i}:")
    print("Dest | Cost | Next Hop")
    for j in range(n):
        print(j, dist[i][j], nexthop[i][j])

src = int(input("Enter source router: "))
dest = int(input("Enter destination router: "))
if dist[src][dest] == INF:
    print("No path exists.")
else:
    path = [src]
    while src != dest:
        src = nexthop[src][dest]
        path.append(src)

    print("Minimum Cost: ", dist[path[0]][dest])
    print("Shortest Path: ", "->".join(map(str, path)))