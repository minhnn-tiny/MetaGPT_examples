import graph
import a_star

def main():
    # Create a graph
    graph = graph.Graph()

    # Add nodes to the graph
    start_node = graph.add_node("start")
    goal_node = graph.add_node("goal")
    node3 = graph.add_node("node3")

    # Add edges to the graph
    edge1 = graph.add_edge("edge1", start_node, goal_node, 1)
    edge2 = graph.add_edge("edge2", start_node, node3, 2)
    edge3 = graph.add_edge("edge3", node3, goal_node, 3)

    # Create an A* search object
    a_star = a_star.AStar(graph, start_node, goal_node)

    # Search for the minimum sweat path
    path = a_star.search()

    # Print the minimum sweat path
    print(path)

if __name__ == "__main__":
    main()
