"""Tests for _2024/_7/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._7.main import (
    parse_equations,
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        mock_file.get_row.return_value = [
            ['190', ' 10 19'],
            ['3267', ' 81 40 27'],
            ['83', ' 17 5'],
            ['156', ' 15 6'],
            ['7290', ' 6 8 6 15'],
            ['161011', ' 16 10 13'],
            ['192', ' 17 8 14'],
            ['21037', ' 9 7 18 13'],
            ['292', ' 11 6 16 20'],
        ]
        
        equations = parse_equations(mock_file)
        result = part1(equations)
        assert result == 3749


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        mock_file.get_row.return_value = [
            ['190', ' 10 19'],
            ['3267', ' 81 40 27'],
            ['83', ' 17 5'],
            ['156', ' 15 6'],
            ['7290', ' 6 8 6 15'],
            ['161011', ' 16 10 13'],
            ['192', ' 17 8 14'],
            ['21037', ' 9 7 18 13'],
            ['292', ' 11 6 16 20'],
        ]
        
        equations = parse_equations(mock_file)
        result = part2(equations)
        assert result == 11387

