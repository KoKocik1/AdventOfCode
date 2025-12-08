from pathlib import Path
import math
from helpers import GetFile, time_and_print
from _2025._8.classes import Vector, VectorDistance, VectorCircuits


def part1(vectors: list[Vector], num_of_circuits: int) -> int:
    vector_distances = []
    for vector in vectors:
        new_vector_distances = calculate_distance(vector, vectors)
        vector_distances.extend(new_vector_distances)
    
    vector_distances.sort(key=lambda x: x.distance)

    vector_circuits = VectorCircuits(vector_distances)
    vector_circuits.create_circuits(num_of_circuits)
    
    vector_circuits.print_circuits()
    return vector_circuits.get_len_circuits()


def part2(vectors: list[Vector]) -> int:
    return 0

def read_data(file: GetFile) -> list[Vector]:
    return [Vector(int(x), int(y), int(z)) for x, y, z in file.get_row()]

def calculate_distance(pointA: Vector, vectors: list[Vector]) -> int:
    vector_distances = []
    a = (pointA.x, pointA.y, pointA.z)
    index = vectors.index(pointA)
    for vector in vectors[index:]:
        if vector == pointA:
            continue
        b = (vector.x, vector.y, vector.z)
        distance = math.dist(a, b)
        vector_distances.append(VectorDistance(pointA, vector, distance))
    return vector_distances

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=',')
    vectors= read_data(file)
    
    result1 = time_and_print("Part 1", part1, vectors, 1000)
    result2 = time_and_print("Part 2", part2, vectors)


if __name__ == "__main__":
    main()
