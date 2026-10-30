INF = 999

def print_table(distance, nextHop, N, title):
    print(f"\n{title}")
    print("="*50)
    for i in range(N):
        print(f"Router {i}:")
        print("  Dest | Cost | Next Hop")
        for j in range(N):
            hop = nextHop[i][j]
            hop_str = str(hop) if hop != -1 else "-"
            print(f"  {j}    | {distance[i][j]:3} | {hop_str}")
        print()

# Get input
N = int(input("Enter number of routers: "))
cost = []
print("Enter cost matrix (use 999 for INF):")
for i in range(N):
    row = list(map(int, input().split()))
    cost.append(row)

# Initialize
distance = [[cost[i][j] for j in range(N)] for i in range(N)]
nextHop = [[-1]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            distance[i][j] = 0
            nextHop[i][j] = i
        elif cost[i][j] != INF:
            nextHop[i][j] = j

# Show initial tables
print_table(distance, nextHop, N, "INITIAL ROUTING TABLES")

# Distance Vector Algorithm
updated = True
iteration = 0
while updated:
    updated = False
    iteration += 1
    print(f"\n--- Iteration {iteration} ---")
    
    for source in range(N):
        for dest in range(N):
            for neighbor in range(N):
                if cost[source][neighbor] != INF and distance[neighbor][dest] != INF:
                    new_cost = cost[source][neighbor] + distance[neighbor][dest]
                    if new_cost < distance[source][dest]:
                        distance[source][dest] = new_cost
                        nextHop[source][dest] = neighbor
                        updated = True
    
    print_table(distance, nextHop, N, f"After Iteration {iteration}")

print("\n" + "="*50)
#print("FINAL ROUTING TABLES")
print_table(distance, nextHop, N, "FINAL ROUTING TABLES")

# Path finding
src = int(input("\nEnter source router: "))
dest = int(input("Enter destination router: "))

if distance[src][dest] == INF:
    print("No path exists!")
else:
    print(f"\nMinimum Cost: {distance[src][dest]}")
    print("Shortest Path:", end=" ")
    path = [src]
    current = src
    while current != dest:
        current = nextHop[current][dest]
        if current == -1:
            print("Path broken!")
            break
        path.append(current)
    print(" -> ".join(map(str, path)))