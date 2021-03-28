def make_graph(nodes, edges):
    graph = {x: [] for x in nodes}
    for idx in range(len(edges)):
        source, sink, cost = edges[idx]
        graph[source].append((sink, cost))


    return graph

def helper(nodes):
    prev_sink = {x: '' for x in nodes}
    prev_sink['u'] = 'u'
    # print('Previous Elements of the key: ', prev_sink)

    distance = {x: float('inf') for x in nodes}
    distance['u'] = 0
    # print('Distance from "u" node: ', distance)

    return prev_sink, distance

def bellamnFord(graph, distance, prev_sink):
    for idx in range(len(graph)):
        print('Iteration '+str(idx)+' Routing Table from "u": ', distance)
        for source in graph:
            for sink, cost in graph[source]:
                if distance[source] + cost < distance[sink]:
                    distance[sink] = distance[source] + cost
                    prev_sink[sink] = source


        if idx == len(graph)-1:
            break

    # print('Final Routing Table: ', distance)
    # print('Previous Table: ', prev_sink)

    return prev_sink, distance

def count_hops(prev_sink, graph_nodes):
    # counting hops
    nodes_hops = {}
    for node in graph_nodes:
        nodes_hops[node] = 0
    # print('Node Hops Router Total: ', nodes_hops)

    for node in prev_sink:
        val = prev_sink[node]
        hop = 1
        while val != 'u':
            val = prev_sink[val]
            hop += 1

        nodes_hops[node] = hop

    nodes_hops['u'] = 0
    # print(nodes_hops)
    return nodes_hops


###################################################################################
"""
Program starts from here.
"""
graph_nodes = ['u', 'v', 'w', 'x', 'y', 'z']
grap_edges = [
    ['u', 'v', 3], ['u', 'x', 1], ['u', 'w', 7],
    ['v', 'w', 1], ['v', 'x', 1], ['v', 'u', 3],
    ['x', 'w', 4], ['x', 'y', 2], ['x', 'v', 1], ['x', 'u', 1],
    ['w', 'x', 4], ['w', 'v', 1], ['w', 'y', 5], ['w', 'z', 6], ['w', 'u', 7],
    ['y', 'x', 2], ['y', 'w', 5], ['y', 'z', 3],
    ['z', 'w', 6], ['z', 'y', 3]
]

# creates graph from the edges
graph = make_graph(graph_nodes, grap_edges)
print('Graph: ')
for node in graph:
    print('Node', node, 'neighbours and cost: ', graph[node])

"""
creates two dictinaries
prev_sink - this stores the node that is before the node that is stored here as the key.
distance - distance of node that is here as key from the source node "u".
"""
prev_sink, distance = helper(graph_nodes)
# print(prev_sink)
# print(distance)
# Applying BellmanFord to the graph given here
print()
print('Routing Table: ')
previous_node_dict, final_distance_dict = bellamnFord(graph, distance, prev_sink)

# Count Hops by backtracking the path
nodes_hops = count_hops(previous_node_dict, graph_nodes)
print()
print('Counting Hop Table: ')
for nodes in nodes_hops:
    print('Hops for',nodes,'is',nodes_hops[nodes])
