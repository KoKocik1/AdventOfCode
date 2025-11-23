"""Tests for _2024/_2/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._2.main import (
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        mock_file.get_row.return_value = [
            ['7', '6', '4', '2', '1'],
            ['1', '2', '7', '8', '9'],
            ['9', '7', '6', '2', '1'],
            ['1', '3', '2', '4', '5'],
            ['8', '6', '4', '4', '1'],
            ['1', '3', '6', '7', '9'],
        ]
        result = part1(mock_file)
        assert result == 2


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        mock_file.get_row.return_value = [
            ['7', '6', '4', '2', '1'],
            ['1', '2', '7', '8', '9'],
            ['9', '7', '6', '2', '1'],
            ['1', '3', '2', '4', '5'],
            ['8', '6', '4', '4', '1'],
            ['1', '3', '6', '7', '9'],
        ]
        result = part2(mock_file)
        assert result == 4
