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
        if before not in self._rules_by_before:
            self._rules_by_before[before] = []
        self._rules_by_before[before].append(rule)

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


class Updates:
    """Collection of update sequences."""

    def __init__(self):
        self.update_lines = []

    def add_update_line(self, line: list[int]):
        """Add a new update line."""
        self.update_lines.append(Update(line))

    def __iter__(self):
        """Allow iteration over updates."""
        return iter(self.update_lines)
