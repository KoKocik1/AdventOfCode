# class Node:
#     input: str
#     outputs: list[str]
    
#     def __init__(self, input: str, outputs: list[str]):
#         self.input = input
#         self.outputs = outputs

#     def __str__(self):
#         return f"{self.input}: {self.outputs}"

#     def __repr__(self):
#         return self.__str__()

class Graph:
    dictionary: dict[str, list[str]]

    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        return f"{self.dictionary}"

    def __repr__(self):
        return self.__str__()
    
    def add_node(self, input: str, outputs: list[str]):
        self.dictionary[input] = outputs
    
    def get_outputs(self, input: str) -> list[str]:
        return self.dictionary.get(input, [])

class Solver:
    graph: Graph
    score: int
    final_node: str
    skip_nodes: list[str]
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.score = 0
        self.skip_nodes = []

    def solve(self, node: str, finish_node: str=None, skip_nodes: list[str]=None) -> int:
        self.score = 0
        if finish_node:
            self.final_node = finish_node
        if skip_nodes:
            self.skip_nodes = skip_nodes
        self.solve_node(node, [])
        return self.score
    
    def solve_node(self, node: str, history: list[str]) -> int:
        history = history.copy()
        if node in history:
            return
        if node == self.final_node:
            print(f"History: {history}")
            self.score += 1
            return
        if self.skip_nodes and node in self.skip_nodes:
            return
        history.append(node)
        outputs = self.graph.get_outputs(node)
        for output in outputs:
            self.solve_node(output, history)
    

class Solver2(Solver):
    
    def solve(self) -> int:
        part1 = super().solve('svr', 'fft', ['dac', 'out'])
        print(f"Part 1: {part1}")
        middle1 = super().solve('fft', 'dac', ['out', 'fft'])
        print(f"Middle 1: {middle1}")
        end1 = super().solve('dac', 'out', ['fft', 'svr'])
        print(f"End 1: {end1}")
        score1 = part1 * middle1 * end1
        print(f"Score 1: {score1}")
        
        
        part2 = super().solve('svr', 'dac', ['fft', 'out'])
        print(f"Part 2: {part2}")
        middle2 = super().solve('dac', 'fft', ['out', 'svr'])
        print(f"Middle 2: {middle2}")
        end2 = super().solve('fft', 'out', ['dac', 'svr'])
        print(f"End 2: {end2}")
        score2 = part2 * middle2 * end2
        print(f"Score 2: {score2}")
        
        
        return score1 + score2
