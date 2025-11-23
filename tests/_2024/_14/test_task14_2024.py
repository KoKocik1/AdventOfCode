"""Tests for _2024/_14/main.py functions."""

import pytest
from unittest.mock import Mock
from _2024._14.main import (
    load_data,
    part1,
)


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        mock_file = Mock()
        # Format: space-delimited, e.g., "p=0,4 v=3,-3"
        mock_file.get_row.return_value = [
            ['p=0,4', 'v=3,-3'],
            ['p=6,3', 'v=-1,-3'],
            ['p=10,3', 'v=-1,2'],
            ['p=2,0', 'v=2,-1'],
            ['p=0,0', 'v=1,3'],
            ['p=3,0', 'v=-2,-2'],
            ['p=7,6', 'v=-1,-3'],
            ['p=3,0', 'v=-1,-2'],
            ['p=9,3', 'v=2,3'],
            ['p=7,3', 'v=-1,2'],
            ['p=2,4', 'v=2,-3'],
            ['p=9,5', 'v=-3,-3'],
        ]
        
        # Use smaller board dimensions for test (default is 101x103)
        board = load_data(mock_file, width=11, height=7)
        result = part1(board, steps=100)
        assert result == 12

