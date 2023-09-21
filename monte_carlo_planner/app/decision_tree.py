import csv
import random
from collections import deque
import argparse
def parse_node_attributes(attr_file_path: str):
    node_attrs = {}
    with open(attr_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header if there is one
        for row in csvreader:
            if row:
                node, node_type, value, probabilities = row
                value = int(value)  # Assuming values are integers
                probabilities = tuple(map(float, probabilities.replace('(', '').replace(')', '').split(',')))
                node_attrs[node] = {'type': node_type, 'value': value, 'probabilities': probabilities}
    return node_attrs

#test parse_node_attributes
attr_file_path = 'D:\\RealProject\\capital_planning_simulator\\SampleData\\decision_nodes.csv'

node_attrs = parse_node_attributes(attr_file_path)
print(node_attrs)

def read_structure_to_graph(struct_file_path, node_attrs):
    graph = {}
    with open(struct_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:
                node = row[0]
                edges = row[1:]
                
                # Check if the node exists in node_attrs
                if node not in node_attrs:
                    print(f"Warning: Node {node} not found in node attributes. Skipping.")
                    continue
                
                # Generate edges
                edges = {edge: node_attrs[node]['probabilities'][i] for i, edge in enumerate(edges)}
                
                # Add to graph
                graph[node] = {'type': node_attrs[node]['type'], 'value': node_attrs[node]['value'], 'edges': edges}
                
    return graph


#test read_structure_to_graph


def print_graph(graph):
    for node, node_data in graph.items():
        node_type = node_data['type']
        edges = node_data['edges']
        print(f"{node} (type: {node_type}) -> {edges}")

struct_file_path = 'D:\RealProject\capital_planning_simulator\SampleData\decision_tree.csv'

graph = read_structure_to_graph(struct_file_path, node_attrs)
print(graph)
print_graph(graph)

current_node = 'A'
A = graph.get(current_node)
edg = A['edges']
for successor, edge_prob in edg.items():
    print(successor,edge_prob)
from collections import deque

from collections import deque
import random

def bfs_based_traverse_graph(graph, start_node, num_iterations):
    master_list = []
    
    for i in range(num_iterations):
        # Uncomment the next line if you want to see which simulation iteration is running
        # print(f"\nSimulation Iteration {i+1}")

        queue = deque([(start_node, 1, 0)])  # Start node, its cumulative probability, and sum_of_values
        value_sum = 0  # Initialize sum for this iteration
        
        while queue:
            current_node, prob, sum_of_values = queue.popleft()
            
            node_data = graph.get(current_node)
            if not node_data:
                # Uncomment the next line if you want to see debug messages
                # print(f"Node {current_node} not found in the graph!")
                continue

            # Update sum_of_values for both 'D' and 'V' types
            sum_of_values += node_data['value']

            # If node type is 'V', break out of loop and store the sum
            if node_data['type'] == 'V':
                value_sum = sum_of_values
                break  # Stop iterating once an end node is reached
                
            edges = node_data['edges']
            if edges:
                # Randomly select one edge to traverse
                successor = random.choice(list(edges.keys()))
                edge_prob = edges[successor]
                next_prob = prob * edge_prob
                next_sum = sum_of_values
                queue.append((successor, next_prob, next_sum))

        # Store the sum for this iteration
        master_list.append(value_sum)
        
    return master_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monte Carlo Planner')

    
    parser.add_argument('node_attributes', help='The node attr file.')
    parser.add_argument('struct', help='The structure file.')
    parser.add_argument('num_iterations', help='Number of iterations.')
    parser.add_argument('start_node', help='Start node.')


    args = parser.parse_args()

    attr_file_path = args.node_attributes
    struct_file_path = args.struct
    num_iterations = int(args.num_iterations)
    start_node = args.start_node

    node_attrs = parse_node_attributes(attr_file_path)
    graph = read_structure_to_graph(struct_file_path, node_attrs)
    num_iterations = 10000
    master_list = bfs_based_traverse_graph(graph, start_node, num_iterations)
    import matplotlib.pyplot as plt
    plt.hist(master_list, bins=50, density=True, alpha=0.6, color='g', label='BFS-based MC')
    plt.xlabel('Sum of Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig('.')
    plt.show()








