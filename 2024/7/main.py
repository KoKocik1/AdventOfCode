from pathlib import Path

from helpers import GetFile
from classes import Equation, Actions


def part1(file: GetFile):
    count = 0
    for row in file.get_row():
        equation = Equation.create_from_string(row[0], row[1].strip())
        actions = Actions()
        if actions.solve_equation(equation):
            count += equation.score
    return count


def part2(file: GetFile):
    count = 0
    for row in file.get_row():
        equation = Equation.create_from_string(row[0], row[1].strip())
        actions = Actions()
        if actions.solve_equation_part2(equation):
            count += equation.score
    return count


def main():
    data_file = Path(__file__).parent / 'data/test.txt'
    file = GetFile(str(data_file), delimiter=':')
    result = part1(file)
    print(result)
    result = part2(file)
    print(result)


if __name__ == "__main__":
    main()
