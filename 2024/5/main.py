from pathlib import Path
from helpers import GetFile
from classes import Rules, Updates, Update


def load_rules(file: GetFile) -> Rules:
    rules = Rules()
    for line in file.get_row():
        rules.add_rule(int(line[0]), int(line[1]))
    return rules


def load_updates(file: GetFile) -> Updates:
    updates = Updates()
    for line in file.get_row():
        line = [int(x) for x in line]
        updates.add_update_line(line)
    return updates


if __name__ == "__main__":
    rules_data_file = Path(__file__).parent / 'data/rules.txt'
    rules_file = GetFile(str(rules_data_file), delimiter='|')
    rules = load_rules(rules_file)

    updates_data_file = Path(__file__).parent / 'data/updates.txt'
    updates_file = GetFile(str(updates_data_file), delimiter=',')
    updates = load_updates(updates_file)

    updates.check_updates(rules)

    total = sum(update.middle_number for update in updates.get_valid_updates())
    print(total)

    updates.repair_updates(rules)
    total = sum(update.middle_number for update in updates.get_invalid_updates())
    print(total)
