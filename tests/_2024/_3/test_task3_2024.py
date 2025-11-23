"""Tests for _2024/_3/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._3.main import (
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        test_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        # GetFile splits by delimiter, so with ' ' delimiter and no spaces, it returns one element
        mock_file.get_row.return_value = [
            [test_string]
        ]
        result = part1(mock_file)
        assert result == 161


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        test_string = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
        # GetFile splits by delimiter, so with ' ' delimiter and no spaces, it returns one element
        mock_file.get_row.return_value = [
            [test_string]
        ]
        result = part2(mock_file)
        assert result == 48

