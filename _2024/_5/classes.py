class Rule:
    """Represents a rule: 'before' page must come before 'after' page."""

    def __init__(self, before: int, after: int):
        self.before = before
        self.after = after

    def __repr__(self) -> str:
        return f"Rule(before={self.before}, after={self.after})"


class Rules:
    """Collection of rules with optimized lookup by 'before' page."""

    def __init__(self):
        self.rules = []
        self._rules_by_before: dict[int, list[Rule]] = {}

    def add_rule(self, before: int, after: int):
        """Add a rule and update the lookup dictionary."""
        rule = Rule(before, after)
        self.rules.append(rule)

        # Update lookup dictionary for O(1) access
        self._rules_by_before.setdefault(before, []).append(rule)

    def get_rules_for_page(self, page: int) -> list[Rule]:
        """Get all rules where the given page is the 'before' page."""
        return self._rules_by_before.get(page, [])


class Update:
    """Represents a sequence of page updates."""

    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    @property
    def middle_number(self) -> int:
        """Get the middle number in the update sequence."""
        return self.numbers[len(self.numbers) // 2]

    def __str__(self) -> str:
        return ', '.join(str(number) for number in self.numbers)

    def __repr__(self) -> str:
        return f"Update({self.numbers})"

    def check_line(self, rules: Rules) -> bool:
        """
        Check if an update sequence violates any rules.

        A rule violation occurs when a 'before' page appears after 
        its corresponding 'after' page in the sequence.

        Returns:
            True if the update is valid (no violations), False otherwise.
        """

        for current_pos, current_page in enumerate(self.numbers):
            # Get all rules where current_page must come before another page
            relevant_rules = rules.get_rules_for_page(current_page)

            for rule in relevant_rules:
                # Check if the 'after' page appears before current_page (violation)
                if rule.after in self.numbers[:current_pos]:
                    return False
        return True

    def repair_line(self, rules: Rules, max_iterations: int = 100):
        """
        Repair violations by swapping pages until valid or max iterations reached.

        Args:
            rules: Rules to check against
            max_iterations: Maximum number of repair attempts to prevent infinite loops
        """
        for _ in range(max_iterations):
            violation_found = False

            for current_pos, current_page in enumerate(self.numbers):
                # Get all rules where current_page must come before another page
                relevant_rules = rules.get_rules_for_page(current_page)

                for rule in relevant_rules:
                    # Check if the 'after' page appears before current_page (violation)
                    if rule.after in self.numbers[:current_pos]:
                        # Find the position of the violating 'after' page
                        after_pos = self.numbers.index(rule.after)
                        # Swap the pages to fix the violation
                        self.numbers[current_pos], self.numbers[after_pos] = (
                            self.numbers[after_pos], self.numbers[current_pos]
                        )
                        violation_found = True
                        break

                if violation_found:
                    break

            # If no violations found, we're done
            if not violation_found or self.check_line(rules):
                break


class Updates:
    """Collection of update sequences."""

    def __init__(self):
        self.valid_updates = []
        self.invalid_updates = []
        self.update_lines = []

    def add_update_line(self, line: list[int]):
        """Add a new update line."""
        self.update_lines.append(Update(line))

    def __iter__(self):
        """Allow iteration over updates."""
        return iter(self.update_lines)

    def check_updates(self, rules: Rules):
        """Separate updates into valid and invalid based on rule violations."""
        self.valid_updates.clear()
        self.invalid_updates.clear()

        for update in self.update_lines:
            if update.check_line(rules):
                self.valid_updates.append(update)
            else:
                self.invalid_updates.append(update)

    @property
    def valid_updates_list(self) -> list[Update]:
        """Get list of valid updates."""
        return self.valid_updates

    @property
    def invalid_updates_list(self) -> list[Update]:
        """Get list of invalid updates."""
        return self.invalid_updates

    def repair_updates(self, rules: Rules):
        for update in self.invalid_updates:
            update.repair_line(rules)
