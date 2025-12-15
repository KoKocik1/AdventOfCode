from pathlib import Path
import math
from helpers import GetFile, time_and_print
from _2025._8.classes import Vector, VectorDistance, VectorCircuits


def calculate_all_distances(vectors: list[Vector]) -> list[VectorDistance]:
    """Calculate distances between all pairs of vectors."""
    vector_distances = []
    for i, vector_a in enumerate(vectors):
        for vector_b in vectors[i + 1:]:
            distance = math.dist(
                (vector_a.x, vector_a.y, vector_a.z),
                (vector_b.x, vector_b.y, vector_b.z)
            )
            vector_distances.append(VectorDistance(vector_a, vector_b, distance))
    return sorted(vector_distances, key=lambda x: x.distance)


def part1(vectors: list[Vector], num_of_circuits: int) -> int:
    vector_distances = calculate_all_distances(vectors)
    vector_circuits = VectorCircuits(vector_distances)
    vector_circuits.create_circuits(num_of_circuits)
    # vector_circuits.print_circuits()
    return vector_circuits.get_len_circuits()


def part2(vectors: list[Vector]) -> int:
    vector_distances = calculate_all_distances(vectors)
    vector_circuits = VectorCircuits(vector_distances, len(vectors))
    vector_circuits.create_circuits()
    # vector_circuits.print_circuits()
    return vector_circuits.get_x1_x2()


def read_data(file: GetFile) -> list[Vector]:
    return [Vector(int(x), int(y), int(z)) for x, y, z in file.get_row()]


def main():
    data_file = Path(__file__).parent / 'data/test.txt'
    file = GetFile(str(data_file), delimiter=',')
    vectors = read_data(file)
    
    result1 = time_and_print("Part 1", part1, vectors, 10)
    result2 = time_and_print("Part 2", part2, vectors)


if __name__ == "__main__":
    main()
