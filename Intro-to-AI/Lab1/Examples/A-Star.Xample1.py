import heapq

# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def heuristic(node, goal):
    return 0  # simple heuristic

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    visited = set()

    while open_list:
        cost, current = heapq.heappop(open_list)

        if current == goal:
            print("Goal reached with shortest cost:", cost)
            return

        if current not in visited:
            visited.add(current)

            for neighbor, weight in graph[current]:
                new_cost = cost + weight
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))

astar('A', 'D')