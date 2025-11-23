from pathlib import Path

from helpers import GetFile
from _2024._13.classes import ButtonFactory, PrizeFactory, Machine, MachineCalculator


def part1(machines: list[Machine]) -> None:
    """Calculate total cost for part 1 with button press limits."""
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        calculator = MachineCalculator(machine)
        cost = calculator.calculate_with_limit()
        if cost > 0:
            total_cost += cost
            prizes_won += 1

    print("Prizes won:", prizes_won)
    print("Minimal total tokens:", total_cost)


def part2(machines: list[Machine]) -> None:
    """Calculate total cost for part 2 without button press limits."""
    total_cost = 0
    prizes_won = 0

    for machine in machines:
        calculator = MachineCalculator(machine)
        cost = calculator.calculate_machine()
        if cost > 0:
            total_cost += cost
            prizes_won += 1

    print("Prizes won:", prizes_won)
    print("Minimal total tokens:", total_cost)


def load_machines(file: GetFile) -> list[Machine]:
    """Load machines from file data."""
    machines: list[Machine] = []
    button_a = None
    button_b = None

    for index, row in enumerate(file.get_row()):
        if index % 4 == 0:
            button_a = ButtonFactory.create_from_string(row[1], row[2], row[3])
        elif index % 4 == 1:
            button_b = ButtonFactory.create_from_string(row[1], row[2], row[3])
        elif index % 4 == 2:
            prize = PrizeFactory.create_from_string(row[1], row[2])
            machines.append(Machine(button_a, button_b, prize))

    return machines


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')

    machines = load_machines(file)
    part1(machines)

    # Adjust prize coordinates for part 2
    prize_offset = 10000000000000
    for machine in machines:
        machine.prize.x += prize_offset
        machine.prize.y += prize_offset

    part2(machines)


if __name__ == "__main__":
    main()
