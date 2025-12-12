from pathlib import Path

from helpers import GetFile, time_and_print
from classes import Graph, Solver, Solver2

def part1(graph: Graph) -> int:
    solver = Solver(graph)
    return solver.solve('you', 'out')


def part2(graph: Graph) -> int:
    solver = Solver2(graph)
    return solver.solve()


def get_data(file: GetFile) -> Graph:
    graph = Graph()
    for line in file.get_row():
        input, outputs = line[0], line[1]
        outputs = outputs.split(' ')
        graph.add_node(input, outputs)
    return graph

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=': ')
    graph = get_data(file)
    
    result1 = time_and_print("Part 1", part1, graph)
    result2 = time_and_print("Part 2", part2, graph)


if __name__ == "__main__":
    main()
