"""Tests for _2025/_2/main.py functions."""

import pytest
import tempfile
import os
from _2025._2.main import part1, part2, get_ranges
from helpers import GetFile


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
        
        array = get_ranges(input_data.split(','))
        result = part1(array)
        assert result == 1227775554


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        input_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
        
        array = get_ranges(input_data.split(','))
        result = part2(array)
        assert result == 4174379265

