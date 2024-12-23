# https://adventofcode.com/2024/day/23

from os import chdir
from os.path import dirname

def load_data(filename):
    chdir(dirname(__file__))

    data_file = open(filename)
    data = data_file.read()
    data_lines = data.split('\n')

    connections = []
    for line in data_lines:
        hyphen = line.find('-')
        host1 = line[:hyphen]
        host2 = line[hyphen + 1:]

        connections.append((host1, host2))
    
    return connections


def build_network(edges):
    network = dict()
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]

        if node1 not in network:
            network[node1] = set()

        if node2 not in network:
            network[node2] = set()
        
        network[node1].add(node2)
        network[node2].add(node1)
    
    return network
    

def fully_connected_groups(graph, size):
    if size == 0:
        return None
    
    if size == 1:
        return {(n,) for n in graph.keys()}

    groups = set()
    smaller_groups = fully_connected_groups(graph, size - 1)
    for group in smaller_groups:
        intersection = None
        for node in group:
            connected_nodes = graph[node]
            if intersection == None:
                intersection = connected_nodes
            else:
                intersection = intersection & connected_nodes
            
        for common in intersection:
            new_group_members = [g for g in group]
            new_group_members.append(common)
            new_group_members.sort()
            new_group = tuple(new_group_members)
            groups.add(new_group)

    print(groups)
    return groups


def p1():
    print('part 1')

    connections = load_data('data.txt')

    network = build_network(connections)

    groups_of_three = fully_connected_groups(network, 3)
    t_groups_of_three = []
    for group in groups_of_three:
        for i in range(3):
            if group[i].startswith('t'):
                t_groups_of_three.append(group)
                break

    print(len(t_groups_of_three))


p1()