from pathlib import Path
from helpers import GetFile
from classes import Rules, Updates, Update


def load_rules(file: GetFile) -> Rules:
    rules = Rules()
    for line in file.get_row():
        rules.add_rule(int(line[0]), int(line[1]))
    return rules


def load_updates(file: GetFile) -> Updates:
    """Load updates from file."""
    updates = Updates()
    for line in file.get_row():
        numbers = [int(x) for x in line]
        updates.add_update_line(numbers)
    return updates


def calculate_total(updates: list) -> int:
    """Calculate the sum of middle numbers from a list of updates."""
    return sum(update.middle_number for update in updates)


if __name__ == "__main__":
    # Load rules
    rules_data_file = Path(__file__).parent / 'data/rules.txt'
    rules_file = GetFile(str(rules_data_file), delimiter='|')
    rules = load_rules(rules_file)

    # Load updates
    updates_data_file = Path(__file__).parent / 'data/updates.txt'
    updates_file = GetFile(str(updates_data_file), delimiter=',')
    updates = load_updates(updates_file)

    # Part 1: Calculate total for valid updates
    updates.check_updates(rules)
    total_valid = calculate_total(updates.valid_updates_list)
    print(total_valid)

    # Part 2: Repair invalid updates and calculate total
    updates.repair_updates(rules)
    total_repaired = calculate_total(updates.invalid_updates_list)
    print(total_repaired)
