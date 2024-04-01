import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.add_node(Node(node1))
        if node2 not in self.nodes:
            self.add_node(Node(node2))
        self.edges[(node1, node2)] = weight

    def get_shortest_path(self, source, destination):
        # Initialize distances to infinity for all nodes
        distances = {node: float('infinity') for node in self.nodes}
        distances[source] = 0

        # Initialize priority queue with source node
        pq = [(0, source)]

        while pq:
            # Get the node with the smallest distance
            current_distance, current_node = heapq.heappop(pq)

            # If we have reached the destination, return the path
            if current_node == destination:
                return self._get_path(source, destination)

            # Iterate over the neighbors of the current node
            for neighbor, weight in self.nodes[current_node].neighbors.items():
                # Calculate the new distance to the neighbor
                new_distance = current_distance + weight

                # If the new distance is shorter than the current distance, update the distance and priority queue
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        # If we have not reached the destination, return None
        return None

    def _get_path(self, source, destination):
        path = [destination]
        current_node = destination
        while current_node != source:
            for neighbor, weight in self.nodes[current_node].neighbors.items():
                if distances[current_node] - weight == distances[neighbor]:
                    path.append(neighbor)
                    current_node = neighbor
                    break
        return path[::-1]


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
