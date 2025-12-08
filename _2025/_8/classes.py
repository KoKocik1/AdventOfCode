class Vector:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    

class VectorDistance:
    pointA: Vector
    pointB: Vector
    distance: int
    
    def __init__(self, pointA: Vector, pointB: Vector, distance: int):
        self.pointA = pointA
        self.pointB = pointB
        self.distance = distance
        
    def __str__(self) -> str:
        return f"VectorDistance({self.pointA}, {self.pointB}, {self.distance})"

    def __repr__(self) -> str:
        return f"VectorDistance({self.pointA}, {self.pointB}, {self.distance})"
    

class VectorCircuits:
    vectorDistances: list[VectorDistance]
    circuits: list[list[Vector]]
    
    def __init__(self, vectorDistances: list[VectorDistance]):
        self.vectorDistances = vectorDistances
        self.circuits = []
        
    def remove_duplicates(self, circuit: list[Vector]):
        for vector in circuit:
            if circuit.count(vector) > 1:
                circuit.remove(vector)
        return circuit
    
    def create_circuits(self, num_of_circuits: int):
        for i in range(num_of_circuits):
            vectorA= self.vectorDistances[i].pointA
            vectorB= self.vectorDistances[i].pointB
            addedA = False
            addedB = False
            aCiruit = None
            bCircuit = None
            should_add_a=False
            should_add_b=False
            #idx = 0
            for circuit in self.circuits:
                # idx += 1
                if not addedA and vectorA in circuit:
                    if addedB:
                        if not vectorB in circuit:
                            circuit.extend(bCircuit)
                            circuit = self.remove_duplicates(circuit)
                            self.circuits.remove(bCircuit)
                    else:
                        if not vectorB in circuit:
                            should_add_b = True
                    aCiruit = circuit
                    addedA = True
                if not addedB and vectorB in circuit:
                    if addedA:
                        if not vectorA in circuit:
                            circuit.extend(aCiruit)
                            circuit = self.remove_duplicates(circuit)
                            self.circuits.remove(aCiruit)
                    else:
                        if not vectorA in circuit:
                            should_add_a = True
                    bCircuit = circuit
                    addedB = True
                if should_add_a:
                    if not vectorA in circuit:
                        circuit.append(vectorA)
                    should_add_a = False
                if should_add_b:
                    if not vectorB in circuit:
                        circuit.append(vectorB)
                    should_add_b = False
            if not addedA and not addedB:
                self.circuits.append([vectorA, vectorB])
            
    
    def get_len_circuits(self) -> int:
        len_circuits = []
        for circuit in self.circuits:
            len_circuits.append(len(circuit))
        len_circuits.sort(reverse=True)
        print(f"[{len_circuits[0]}, {len_circuits[1]}, {len_circuits[2]}]")
        return len_circuits[0] * len_circuits[1] * len_circuits[2]
    
    def print_circuits(self):
        for circuit in self.circuits:
            print(circuit)
    
    def __str__(self) -> str:
        return f"VectorCircuits({self.vectorDistances})"
    
    def __repr__(self) -> str:
        return f"VectorCircuits({self.vectorDistances})"
    
    def __eq__(self, other: 'VectorCircuits') -> bool:
        return self.vectorDistances == other.vectorDistances