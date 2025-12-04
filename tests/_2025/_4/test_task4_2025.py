"""Tests for _2025/_4/main.py functions."""

import pytest
import tempfile
import os
from _2025._4.main import part1, part2
from helpers import GetFile, Board


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='')
            array = file.get_2d_array()
            board = Board(array)
            
            result = part1(board)
            
            assert result == 13
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='')
            array = file.get_2d_array()
            board = Board(array)
            
            result = part2(board)
            
            assert result == 43
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)

