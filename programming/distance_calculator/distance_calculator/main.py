import dijkstra

def main():
    # Create a graph
    graph = dijkstra.Graph()

    # Add nodes to the graph
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")

    # Add edges to the graph
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 3)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 5)
    graph.add_edge("C", "E", 6)
    graph.add_edge("D", "E", 7)

    # Get the shortest path between two nodes
    shortest_path = graph.get_shortest_path("A", "E")

    # Print the shortest path
    print(shortest_path)

if __name__ == "__main__":
    main()
