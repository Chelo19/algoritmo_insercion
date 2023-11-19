import numpy as np

def euclidean_distance(node1, node2):
    x1, y1 = node1[1], node1[2]
    x2, y2 = node2[1], node2[2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

with open('6nodes.txt', 'r') as file:
    lines = file.readlines()

start_idx = lines.index('NODE_COORD\n') + 1

nodes = []
for line in lines[start_idx:]:
    data = line.strip().split()
    if len(data) == 3:
        node = [int(data[0]), int(data[1]), int(data[2])]
        nodes.append(node)

def cheapest_insertion(nodes):
    n = len(nodes)
    route = [nodes[0]]
    remaining_nodes = nodes[1:]

    while remaining_nodes:
        min_distance = np.inf
        min_index = -1

        for i, node in enumerate(remaining_nodes):
            for j in range(len(route)):
                dist_increase = euclidean_distance(route[j], node) + euclidean_distance(node, route[(j+1) % len(route)]) - euclidean_distance(route[j], route[(j+1) % len(route)])

                if dist_increase < min_distance:
                    min_distance = dist_increase
                    min_index = i
                    insertion_point = j + 1

        route.insert(insertion_point, remaining_nodes[min_index])
        del remaining_nodes[min_index]

    return route

optimal_route = cheapest_insertion(nodes)

total_distance = sum(euclidean_distance(optimal_route[i], optimal_route[(i+1) % len(optimal_route)]) for i in range(len(optimal_route)))

print("Ruta óptima:")
print(", ".join(str(node[0]) for node in optimal_route))
print(f"Distancia total: {total_distance}")