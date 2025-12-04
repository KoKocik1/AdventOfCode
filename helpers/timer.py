"""Timer helper for measuring function execution time."""

import time
from typing import Callable, TypeVar, Any

T = TypeVar('T')


def time_function(func: Callable[..., T], *args: Any, **kwargs: Any) -> tuple[T, float]:
    """Measure the execution time of a function.
    
    Args:
        func: The function to measure
        *args: Positional arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
    
    Returns:
        A tuple containing (function_result, elapsed_time_in_seconds)
    
    Example:
        >>> result, elapsed = time_function(part1, array)
        >>> print(f"Result: {result}, Time: {elapsed:.4f}s")
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def print_timed_result(name: str, result: Any, elapsed_time: float) -> None:
    """Print a formatted result with timing information.
    
    Args:
        name: Name/description of the timed operation (e.g., "Part 1")
        result: The result to display
        elapsed_time: The elapsed time in seconds
    
    Example:
        >>> result, elapsed = time_function(part1, array)
        >>> print_timed_result("Part 1", result, elapsed)
        Part 1: 1234 (Time: 0.0234 seconds)
    """
    print(f"{name}: {result} (Time: {elapsed_time:.4f} seconds)")


def time_and_print(name: str, func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """Measure function execution time and print the result.
    
    This is a convenience function that combines time_function and print_timed_result.
    
    Args:
        name: Name/description of the timed operation (e.g., "Part 1")
        func: The function to measure
        *args: Positional arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
    
    Returns:
        The result of the function
    
    Example:
        >>> result = time_and_print("Part 1", part1, array)
        Part 1: 1234 (Time: 0.0234 seconds)
    """
    result, elapsed_time = time_function(func, *args, **kwargs)
    print_timed_result(name, result, elapsed_time)
    return result

