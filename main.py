# Import necessary libraries
import heapq   # Import heapq for the priority queue
import networkx as nx   # Import networkx for graph representation
import matplotlib.pyplot as plt   # Import matplotlib.pyplot for graph visualization

# Define Dijkstra's algorithm to find shortest paths
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}   # Initialize distances to vertices as infinity
    distances[start] = 0   # Set distance to the starting vertex as 0
    priority_queue = [(0, start)]   # Use a priority queue to efficiently explore the graph
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)   # Pop the vertex with the smallest distance
        
        if current_distance > distances[current_vertex]:
            continue   # Skip if the current distance is greater than the recorded distance
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight   # Calculate the distance to the neighbor
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance   # Update the distance if a shorter path is found
                heapq.heappush(priority_queue, (distance, neighbor))   # Add to the priority queue

    return distances   # Return the computed distances

# Function to input a weighted graph from the user
def input_graph():
    graph = {}   # Initialize an empty graph
    vertices = input("Enter the vertices (comma-separated): ").split(',')   # Input vertices from the user
    
    for vertex in vertices:
        graph[vertex] = {}   # Initialize an empty dictionary for each vertex
        
    for vertex in graph:
        neighbors_str = input(f"Enter neighbors and distances for vertex {vertex} (neighbor1,distance1,neighbor2,distance2,...): ")
        neighbors_list = neighbors_str.split(',')   # Input neighbors and distances for each vertex
        
        for i in range(0, len(neighbors_list), 2):
            neighbor, distance = neighbors_list[i], float(neighbors_list[i + 1])
            graph[vertex][neighbor] = distance   # Add neighbors and distances to the graph

    return graph   # Return the created graph

# Create and visualize the graph
def visualize_graph(graph):
    G = nx.Graph()   # Create an empty graph
    
    for vertex, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            G.add_edge(vertex, neighbor, weight=distance)   # Add edges with weights to the graph
    
    pos = nx.spring_layout(G)   # Set the layout for graph visualization
    labels = nx.get_edge_attributes(G, 'weight')   # Get edge weights for labeling
    
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)   # Draw the graph
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)   # Label the edges
    
    plt.axis('off')   # Turn off axis labels
    plt.show()   # Display the graph

# Example usage
if __name__ == "__main__":
    graph = input_graph()   # Get user input for the graph
    start_vertex = input("Enter the starting vertex: ")   # Get user input for the starting vertex
    shortest_distances = dijkstra(graph, start_vertex)   # Run Dijkstra's algorithm
    
    for vertex, distance in shortest_distances.items():
        print(f'Shortest distance from {start_vertex} to {vertex} is {distance}')   # Print the shortest distances
    
    visualize_graph(graph)   # Visualize the graph
