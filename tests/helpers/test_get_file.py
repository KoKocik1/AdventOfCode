"""Tests for helpers.get_file module."""

import pytest
import tempfile
import os
from helpers.get_file import GetFile


class TestGetFile:
    """Tests for GetFile class."""

    def test_get_row_with_space_delimiter(self):
        """Test get_row with space delimiter."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("hello world\nfoo bar\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            rows = list(file_reader.get_row())
            assert rows == [['hello', 'world'], ['foo', 'bar']]
        finally:
            os.unlink(temp_path)

    def test_get_row_with_empty_delimiter(self):
        """Test get_row with empty delimiter (splits into characters)."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("abc\ndef\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter='')
            rows = list(file_reader.get_row())
            assert rows == [['a', 'b', 'c'], ['d', 'e', 'f']]
        finally:
            os.unlink(temp_path)

    def test_get_row_with_custom_delimiter(self):
        """Test get_row with custom delimiter."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("a|b|c\nd|e|f\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter='|')
            rows = list(file_reader.get_row())
            assert rows == [['a', 'b', 'c'], ['d', 'e', 'f']]
        finally:
            os.unlink(temp_path)

    def test_get_row_with_empty_lines(self):
        """Test get_row with empty lines."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("a b\n\nc d\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            rows = list(file_reader.get_row())
            assert rows == [['a', 'b'], [''], ['c', 'd']]
        finally:
            os.unlink(temp_path)

    def test_get_row_strips_whitespace(self):
        """Test that get_row strips whitespace from lines."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("  a b  \n  c d  \n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            rows = list(file_reader.get_row())
            assert rows == [['a', 'b'], ['c', 'd']]
        finally:
            os.unlink(temp_path)

    def test_get_2d_array(self):
        """Test get_2d_array method."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("a b\nc d\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            array = file_reader.get_2d_array()
            assert array == [['a', 'b'], ['c', 'd']]
        finally:
            os.unlink(temp_path)

    def test_get_2d_array_empty_delimiter(self):
        """Test get_2d_array with empty delimiter."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("ab\ncd\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter='')
            array = file_reader.get_2d_array()
            assert array == [['a', 'b'], ['c', 'd']]
        finally:
            os.unlink(temp_path)

    def test_get_row_generator_behavior(self):
        """Test that get_row returns a generator."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("a b\nc d\n")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            generator = file_reader.get_row()
            assert hasattr(generator, '__iter__')
            assert hasattr(generator, '__next__')
            
            # Can iterate multiple times by recreating
            rows1 = list(file_reader.get_row())
            rows2 = list(file_reader.get_row())
            assert rows1 == rows2
        finally:
            os.unlink(temp_path)

    def test_get_row_with_single_line(self):
        """Test get_row with single line file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("a b c")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            rows = list(file_reader.get_row())
            assert rows == [['a', 'b', 'c']]
        finally:
            os.unlink(temp_path)

    def test_get_row_with_empty_file(self):
        """Test get_row with empty file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("")
            temp_path = f.name

        try:
            file_reader = GetFile(temp_path, delimiter=' ')
            rows = list(file_reader.get_row())
            assert rows == []
        finally:
            os.unlink(temp_path)

