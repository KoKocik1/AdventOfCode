import networkx as nx
from collections import deque
class Node:
    name: str
    parents: set['Node']
    childrens: set['Node']
    level: int
    
    def __init__(self, name: str):
        self.name = name
        self.childrens = set()
        self.parents = set()
        self.level = -1
    
    def add_parent(self, parent: 'Node'):
        self.parents.add(parent)
        parent.childrens.add(self)
    
    def add_child(self, child: 'Node'):
        self.childrens.add(child)
        child.add_parent(self)
    
    def set_children(self, children: list['Node']):
        self.childrens = set(children)
        for child in children:
            child.add_parent(self)
    
    def get_childrens(self) -> list['Node']:
        return list(self.childrens)
    
    def get_parent(self) -> 'Node':
        return self.parent
    
    def set_level(self, level: int):
        if self.level < level:
            self.level = level
            return True
        return False
    
    def __eq__(self, other: 'Node') -> bool:
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

class Graph:
    graph: nx.DiGraph
    nodes: dict[str, Node]
    
    def __init__(self):
        self.nodes = {}
        self.graph = nx.DiGraph()

    def set_nodes(self, nodes: dict[str, Node]):
        self.nodes = nodes
    
    def get_node(self, name: str) -> Node | None:
        if name not in self.nodes:
            return None
        return self.nodes[name]
    
    def set_levels(self):
        visited = set()
        
        first_node = self.get_node('svr')
        queue = deque([(first_node, 0)])
        while queue:
            node, level = queue.popleft()
            switched = node.set_level(level)
            if switched:
                for child in node.get_childrens():
                    if child not in visited:
                        visited.add(child)
                        queue.append((child, level + 1))

class Solver:
    graph: Graph
    score: int
    final_node: Node
    failed_nodes: set[Node]
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.score = 0

    def solve(self, node: Node, finish_node: Node) -> int:
        if node.level > finish_node.level:
            return 0
        self.score = 0
        self.failed_nodes = set()
        self.final_node = finish_node
        self.solve_node(node)
        return self.score
    
    def solve_node(self, node: Node) -> int:
        queue = deque([node])
        while queue:
            node = queue.pop()
            if node.level > self.final_node.level:
                self.failed_nodes.add(node)
                continue
            if node in self.failed_nodes:
                continue
            
            if node == self.final_node:
                self.score += 1
                continue
            childrens = node.get_childrens()
            any_child = False
            for child in childrens:
                if child not in self.failed_nodes:
                    queue.append(child)
                    any_child = True
            if not any_child:
                self.failed_nodes.add(node)
    

class Solver2(Solver):
    
    def solve(self) -> int:
        svr = self.graph.get_node('svr')
        fft = self.graph.get_node('fft')
        dac = self.graph.get_node('dac')
        out = self.graph.get_node('out')
        
        score1 = 0
        score2 = 0
        
        #becouse:
        #svr.level <= fft.level <= dac.level <= out.level
        
        part1 = super().solve(svr, fft)
        middle1 = super().solve(fft, dac)
        end1 = super().solve(dac, out)
        score1 = part1 * middle1 * end1
        print(f"{score1} = Start({part1}) * Middle({middle1}) * End({end1})")
        
        return score1 + score2
