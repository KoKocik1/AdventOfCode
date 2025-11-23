"""Tests for _2024/_13/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._13.main import (
    load_machines,
)
from _2024._13.classes import MachineCalculator


def calculate_part1_total(machines):
    """Helper function to calculate part1 total cost."""
    total_cost = 0
    for machine in machines:
        calculator = MachineCalculator(machine)
        cost = calculator.calculate_with_limit()
        if cost > 0:
            total_cost += cost
    return total_cost


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        # Format: Button A, Button B, Prize, empty line (repeated)
        mock_file.get_row.return_value = [
            ['Button', 'A:', 'X+94,', 'Y+34'],  # index 0: Button A
            ['Button', 'B:', 'X+22,', 'Y+67'],  # index 1: Button B
            ['Prize:', 'X=8400,', 'Y=5400'],    # index 2: Prize
            [],                                   # index 3: empty
            ['Button', 'A:', 'X+26,', 'Y+66'],  # index 4: Button A
            ['Button', 'B:', 'X+67,', 'Y+21'],  # index 5: Button B
            ['Prize:', 'X=12748,', 'Y=12176'],  # index 6: Prize
            [],                                   # index 7: empty
            ['Button', 'A:', 'X+17,', 'Y+86'],  # index 8: Button A
            ['Button', 'B:', 'X+84,', 'Y+37'],  # index 9: Button B
            ['Prize:', 'X=7870,', 'Y=6450'],    # index 10: Prize
            [],                                   # index 11: empty
            ['Button', 'A:', 'X+69,', 'Y+23'],  # index 12: Button A
            ['Button', 'B:', 'X+27,', 'Y+71'],  # index 13: Button B
            ['Prize:', 'X=18641,', 'Y=10279'],  # index 14: Prize
            [],                                   # index 15: empty
        ]
        
        machines = load_machines(mock_file)
        total_cost = calculate_part1_total(machines)
        assert total_cost == 480

