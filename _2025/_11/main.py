from pathlib import Path

from helpers import GetFile, time_and_print
from classes import Graph, Solver, Solver2, Node

def part1(graph: Graph) -> int:
    solver = Solver(graph)
    you = graph.get_node('you')
    out = graph.get_node('out')
    if you is None or out is None:
        return 0
    return solver.solve(you, out)


def part2(graph: Graph) -> int:
    solver = Solver2(graph)
    return solver.solve()

def add_node(nodes: dict[str, Node], name: str) -> Node:
    if name not in nodes:
        nodes[name] = Node(name)
    return nodes[name]
        
def get_data(file: GetFile) -> Graph:
    nodes = dict[str, Node]()
    graph = Graph()
    for line in file.get_row():
        input, outputs = line[0], line[1]
        outputs = outputs.split(' ')
        node = add_node(nodes, input)
        for output in outputs:
            child = add_node(nodes, output)
            child.add_parent(node)
    graph.set_nodes(nodes)
    graph.set_levels()

    #graph.create_graph()
    return graph

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=': ')
    graph = get_data(file)
    
    result1 = time_and_print("Part 1", part1, graph)
    result2 = time_and_print("Part 2", part2, graph)


if __name__ == "__main__":
    main()
