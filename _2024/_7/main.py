from pathlib import Path

from helpers import GetFile
from _2024._7.classes import Equation, Actions


def parse_equations(file: GetFile) -> list[Equation]:
    equations: list[Equation] = []
    for row in file.get_row():
        equations.append(Equation.create_from_string(row[0], row[1].strip()))
    return equations


def part1(equations: list[Equation]) -> int:
    count = 0
    actions = Actions()
    return sum(eq.score for eq in equations if actions.solve_equation(eq))


def part2(equations: list[Equation]) -> int:
    count = 0
    actions = Actions(allow_concat=True)
    return sum(eq.score for eq in equations if actions.solve_equation(eq))


def main():
    data_file = Path(__file__).parent / 'data/test.txt'
    file = GetFile(str(data_file), delimiter=':')
    equations = parse_equations(file)
    result = part1(equations)
    print(result)
    result = part2(equations)
    print(result)


if __name__ == "__main__":
    main()
