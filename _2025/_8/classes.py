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
    distance: float
    
    def __init__(self, pointA: Vector, pointB: Vector, distance: float):
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
    last_x1: int
    last_x2: int

    def __init__(self, vectorDistances: list[VectorDistance], num_of_vectors: int = 0):
        self.vectorDistances = vectorDistances
        self.circuits: list[list[Vector]] = []
        self.last_x1 = 0
        self.last_x2 = 0
        self.num_of_vectors = num_of_vectors
        
    def remove_duplicates(self, circuit: list[Vector]) -> list[Vector]:
        """Remove duplicate vectors from a circuit while preserving order."""
        seen = set()
        result = []
        for vector in circuit:
            if vector not in seen:
                seen.add(vector)
                result.append(vector)
        circuit.clear()
        circuit.extend(result)
        return circuit
    
    def create_circuits(self, num_of_circuits: int = 0):
        """Create circuits by connecting vectors based on their distances."""
        if num_of_circuits == 0:
            num_of_circuits = len(self.vectorDistances)
        
        for i in range(num_of_circuits):
            vector_a = self.vectorDistances[i].pointA
            vector_b = self.vectorDistances[i].pointB
            
            circuit_a = None
            circuit_b = None
            found_a = False
            found_b = False
            should_add_a_to_current = False
            should_add_b_to_current = False
            
            for circuit in self.circuits:
                # Check if vector_a is in this circuit
                if not found_a and vector_a in circuit:
                    circuit_a = circuit
                    found_a = True
                    
                    # If vector_b was already found in a different circuit, merge them
                    if found_b:
                        if circuit_b != circuit and vector_b not in circuit:
                            self._merge_circuit_into(circuit_b, circuit)
                    # Otherwise, mark that we should add vector_b to this circuit
                    elif vector_b not in circuit:
                        should_add_b_to_current = True
                
                # Check if vector_b is in this circuit
                if not found_b and vector_b in circuit:
                    circuit_b = circuit
                    found_b = True
                    
                    # If vector_a was already found in a different circuit, merge them
                    if found_a:
                        if circuit_a != circuit and vector_a not in circuit:
                            self._merge_circuit_into(circuit_a, circuit)
                    # Otherwise, mark that we should add vector_a to this circuit
                    elif vector_a not in circuit:
                        should_add_a_to_current = True
                
                # Add vectors to the current circuit if flags are set
                # (This handles adding vectors to circuits found in this iteration)
                if should_add_a_to_current:
                    if vector_a not in circuit:
                        circuit.append(vector_a)
                    should_add_a_to_current = False
                
                if should_add_b_to_current:
                    if vector_b not in circuit:
                        circuit.append(vector_b)
                    should_add_b_to_current = False
                
                # Early exit check for part2
                if self._check_early_exit(vector_a, vector_b):
                    return
            
            # If neither vector was found in any circuit, create a new one
            if not found_a and not found_b:
                self.circuits.append([vector_a, vector_b])
    
    def _merge_circuit_into(self, source_circuit: list[Vector], target_circuit: list[Vector]):
        """Merge source_circuit into target_circuit and remove source_circuit."""
        target_circuit.extend(source_circuit)
        self.remove_duplicates(target_circuit)
        if source_circuit in self.circuits:
            self.circuits.remove(source_circuit)
    
    def _check_early_exit(self, vector_a: Vector, vector_b: Vector) -> bool:
        """Check if we should stop early (for part2 when all vectors are connected)."""
        if (self.num_of_vectors > 0 and 
            len(self.circuits) == 1 and 
            len(self.circuits[0]) == self.num_of_vectors and 
            self.last_x1 == 0 and 
            self.last_x2 == 0):
            self.last_x1 = vector_a.x
            self.last_x2 = vector_b.x
            # print(f"[{self.last_x1}, {self.last_x2}]")
            return True
        return False
    def get_len_circuits(self) -> int:
        """Get the product of the lengths of the three largest circuits."""
        if not self.circuits:
            return 0
        
        len_circuits = [len(circuit) for circuit in self.circuits]
        len_circuits.sort(reverse=True)
        
        # Ensure we have at least 3 values, pad with 1 if needed
        while len(len_circuits) < 3:
            len_circuits.append(1)
        
        top_three = len_circuits[:3]
        # print(f"[{top_three[0]}, {top_three[1]}, {top_three[2]}]")
        return top_three[0] * top_three[1] * top_three[2]
    
    def get_x1_x2(self) -> int:
        return self.last_x1 * self.last_x2
    
    def print_circuits(self) -> None:
        """Print all circuits for debugging purposes."""
        for circuit in self.circuits:
            print(circuit)
    
    def __str__(self) -> str:
        return f"VectorCircuits({self.vectorDistances})"
    
    def __repr__(self) -> str:
        return f"VectorCircuits({self.vectorDistances})"
    
    def __eq__(self, other: 'VectorCircuits') -> bool:
        return self.vectorDistances == other.vectorDistances