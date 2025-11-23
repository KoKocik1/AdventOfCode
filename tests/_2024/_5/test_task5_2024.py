"""Tests for _2024/_5/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._5.main import (
    load_rules,
    load_updates,
    calculate_total,
)
from _2024._5.classes import Rules, Updates


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Rules data (pipe-delimited)
        rules_mock = Mock()
        rules_mock.get_row.return_value = [
            ['47', '53'],
            ['97', '13'],
            ['97', '61'],
            ['97', '47'],
            ['75', '29'],
            ['61', '13'],
            ['75', '53'],
            ['29', '13'],
            ['97', '29'],
            ['53', '29'],
            ['61', '53'],
            ['97', '53'],
            ['61', '29'],
            ['47', '13'],
            ['75', '47'],
            ['97', '75'],
            ['47', '61'],
            ['75', '61'],
            ['47', '29'],
            ['75', '13'],
            ['53', '13'],
        ]
        rules = load_rules(rules_mock)

        # Updates data (comma-delimited)
        updates_mock = Mock()
        updates_mock.get_row.return_value = [
            ['75', '47', '61', '53', '29'],
            ['97', '61', '53', '29', '13'],
            ['75', '29', '13'],
            ['75', '97', '47', '61', '53'],
            ['61', '13', '29'],
            ['97', '13', '75', '29', '47'],
        ]
        updates = load_updates(updates_mock)

        # Part 1: Calculate total for valid updates
        updates.check_updates(rules)
        total_valid = calculate_total(updates.valid_updates_list)
        assert total_valid == 143


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        # Rules data (pipe-delimited)
        rules_mock = Mock()
        rules_mock.get_row.return_value = [
            ['47', '53'],
            ['97', '13'],
            ['97', '61'],
            ['97', '47'],
            ['75', '29'],
            ['61', '13'],
            ['75', '53'],
            ['29', '13'],
            ['97', '29'],
            ['53', '29'],
            ['61', '53'],
            ['97', '53'],
            ['61', '29'],
            ['47', '13'],
            ['75', '47'],
            ['97', '75'],
            ['47', '61'],
            ['75', '61'],
            ['47', '29'],
            ['75', '13'],
            ['53', '13'],
        ]
        rules = load_rules(rules_mock)

        # Updates data (comma-delimited)
        updates_mock = Mock()
        updates_mock.get_row.return_value = [
            ['75', '47', '61', '53', '29'],
            ['97', '61', '53', '29', '13'],
            ['75', '29', '13'],
            ['75', '97', '47', '61', '53'],
            ['61', '13', '29'],
            ['97', '13', '75', '29', '47'],
        ]
        updates = load_updates(updates_mock)

        # Part 1: Check updates first to separate valid/invalid
        updates.check_updates(rules)
        
        # Part 2: Repair invalid updates and calculate total
        updates.repair_updates(rules)
        total_repaired = calculate_total(updates.invalid_updates_list)
        assert total_repaired == 123

