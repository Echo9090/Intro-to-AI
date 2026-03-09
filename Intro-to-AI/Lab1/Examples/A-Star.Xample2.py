import heapq

# Graph representation
graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 4)],
    'B': [('C', 1)],
    'C': [('G', 3)],
    'G': []
}

def heuristic(node, goal):
    return 0  # simple heuristic

def astar(start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_cost = cost_so_far[current] + weight

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    print("Shortest path:", path)
    print("Total cost:", cost_so_far[goal])


astar('S', 'G')