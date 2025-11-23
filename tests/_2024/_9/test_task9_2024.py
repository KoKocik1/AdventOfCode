"""Tests for _2024/_9/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._9.main import (
    part1,
    part2,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        # The string is split into characters when delimiter is ''
        test_string = '2333133121414131402'
        mock_file.get_row.return_value = [list(test_string)]
        
        result = part1(mock_file)
        assert result == 1928


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        # The string is split into characters when delimiter is ''
        test_string = '2333133121414131402'
        mock_file.get_row.return_value = [list(test_string)]
        
        result = part2(mock_file)
        assert result == 2858

