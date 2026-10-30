
n = int(input("Enter routers: "))
cost = [list(map(int, input().split())) for i in range(n)]
dist = [r[:] for r in cost]

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print("Final Routing Tables:")
for i in range(n):
    print("Router", i, dist[i])

s = int(input("Source: "))
d = int(input("Destination: "))
print("Minimum Cost:", dist[s][d])
    