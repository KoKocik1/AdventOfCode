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


def check_updates(rules: Rules, updates: Updates) -> tuple[list[Update], list[Update]]:
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if check_line(rules, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates


def check_line(rules: Rules, update: Update) -> bool:
    """
    Check if an update sequence violates any rules.

    A rule violation occurs when a 'before' page appears after 
    its corresponding 'after' page in the sequence.

    Returns:
        True if the update is valid (no violations), False otherwise.
    """
    numbers = update.numbers

    for current_pos, current_page in enumerate(numbers):
        # Get all rules where current_page must come before another page
        relevant_rules = rules.get_rules_for_page(current_page)

        for rule in relevant_rules:
            # Check if the 'after' page appears before current_page (violation)
            if rule.after in numbers[:current_pos]:
                return False
    return True


if __name__ == "__main__":
    rules_data_file = Path(__file__).parent / 'data/rules.txt'
    rules_file = GetFile(str(rules_data_file), delimiter='|')
    rules = load_rules(rules_file)

    updates_data_file = Path(__file__).parent / 'data/updates.txt'
    updates_file = GetFile(str(updates_data_file), delimiter=',')
    updates = load_updates(updates_file)

    valid_updates, invalid_updates = check_updates(rules, updates)

    total = sum(update.middle_number for update in valid_updates)

    print(total)
