"""Tests for _2025/_6/main.py functions."""

import pytest
import tempfile
import os
from _2025._6.main import part1, part2, get_part1_data, get_part2_data
from helpers import GetFile


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter=' ')
            column_scores = get_part1_data(file)
            
            result = part1(column_scores)
            
            assert result == 4277556
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
        
        # Create a temporary file with the test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(input_data)
            temp_path = f.name
        
        try:
            file = GetFile(temp_path, delimiter='')
            array = file.get_2d_array(False)
            column_scores = get_part2_data(array)
            
            result = part2(column_scores)
            
            assert result == 3263827
        finally:
            # Clean up the temporary file
            os.unlink(temp_path)

