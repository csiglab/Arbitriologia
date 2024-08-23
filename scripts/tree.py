import matplotlib.pyplot as plt
import networkx as nx
import collections

paths  = [
    "00",
    "01",
    "0101",
    "01",
    "0001",
    "0102",
    "01",
    "0001",
    "02",  # Poder Ejecutivo
    "0201",
    "01"
]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.down = None
        self.up = None    

    def __repr__(self):
        return f"Node({self.value})"

def build_graph(paths):
    assert len(paths) > 0, "Error: The 'paths' list should not be empty. Please ensure that it contains elements."
    main  = Node(paths[0])
    graph  = main

    for item in paths[1:]:
        node  = Node(item)
        add_node(node, main)
        graph = node
    
    return main

def add_node(node, graph):
    """
        How to add the node to the structure?
        This is a semi wicked problem?
        graph: last node

        Map:
             -> Node -> down, right, up(n level)
             -> Place The Node In That Point
        
        is len(node) > len(last node) || val(node) > val(last node) -> son
    """

    def down(node, graph):
        graph.down = node
        node.up = graph
    
    def right(node, graph):
        graph.right = node
        node.left  = graph

    def up(node, graph):
        pass

    action  = None
    actions = {
        "down":  down,
        "right": right,
        "up":    up
    }

    if len(node.value) > len(graph.value):
        action = actions['down']
    elif len(node.value) == len(graph.value):
        action = actions['right']
    else:   
        action = actions['up']
    
    action(node, graph)

def traverse(start_node):
    visited = set()
    queue = collections.deque([start_node])
    nodes = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            nodes.append(node)

            # Add adjacent nodes to the queue
            for neighbor in (node.left, node.right, node.up, node.down):
                if neighbor and neighbor not in visited:
                    queue.append(neighbor)
    
    return nodes

def generate_image(nodes, filename='graph.png'):
    G = nx.DiGraph()
    pos = {}  # Node positions
    
    for node in nodes:
        G.add_node(node.value)
        if node.left:
            G.add_edge(node.value, node.left.value)
        if node.right:
            G.add_edge(node.value, node.right.value)
        if node.up:
            G.add_edge(node.value, node.up.value)
        if node.down:
            G.add_edge(node.value, node.down.value)
    
    # Create a layout for the nodes
    pos = nx.spring_layout(G)

        # Draw the graph
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, font_weight='bold')
    plt.title('Graph Visualization')

    # Save the image
    plt.savefig(filename)
    plt.close()


graph  =  build_graph(paths)
nodes  = traverse(graph)
print(nodes)
generate_image(nodes)