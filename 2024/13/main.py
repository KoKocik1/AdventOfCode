from pathlib import Path

from helpers import GetFile
from classes import ButtonFactory, PrizeFactory, Mashine, MashineCalculator


def part1(mashines: list[Mashine]) -> int:
    total_cost = 0
    prizes_won = 0
    for mashine in mashines:
        calculator = MashineCalculator(mashine)
        cost = calculator.calculate_with_limit()
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    print("Prizes won:", prizes_won)
    print("Minimal total tokens:", total_cost)


def part2(mashines: list[Mashine]) -> int:
    total_cost = 0
    prizes_won = 0
    for mashine in mashines:
        calculator = MashineCalculator(mashine)
        cost = calculator.calculate_mashine()
        if cost is not None:
            total_cost += cost
            prizes_won += 1

    print("Prizes won:", prizes_won)
    print("Minimal total tokens:", total_cost)


def load_mashines(file: GetFile) -> list[Mashine]:
    mashines: list[Mashine] = []
    for index, row in enumerate(file.get_row()):
        if index % 4 == 0:
            button_a = ButtonFactory.create_from_string(row[1], row[2], row[3])
        elif index % 4 == 1:
            button_b = ButtonFactory.create_from_string(row[1], row[2], row[3])
        elif index % 4 == 2:
            prize = PrizeFactory.create_from_string(row[1], row[2])
            mashines.append(Mashine(button_a, button_b, prize))

    return mashines


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')

    mashines = load_mashines(file)
    part1(mashines)

    increse = 10000000000000
    for mashine in mashines:
        mashine.prize.x = mashine.prize.x + increse
        mashine.prize.y = mashine.prize.y + increse
    part2(mashines)


if __name__ == "__main__":
    main()
