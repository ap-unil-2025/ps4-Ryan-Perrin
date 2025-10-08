"""
Problem 1: List Operations and Comprehensions
Practice working with Python lists - creating, modifying, filtering, and transforming them.
"""


def create_number_list(start, end):
    """
    Create a list of numbers from start to end (inclusive).

    Args:
        start (int): Starting number
        end (int): Ending number

    Returns:
        list: List of numbers from start to end

    Example:
        >>> create_number_list(1, 5)
        [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    # Hint: Use range() and convert to list
    numbers = list(range(start, end +1)) # end+1 to include end
    return numbers
    pass


def filter_even_numbers(numbers):
    """
    Return a new list containing only the even numbers.

    Args:
        numbers (list): List of integers

    Returns:
        list: List of even numbers only

    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    # TODO: Implement this function
    # You can use a loop or list comprehension
    even_numbers = [n for n in numbers if n % 2 == 0] # create a new list containing event numbers. n%2 to pick only even numbers
    return even_numbers
    pass


def square_numbers(numbers):
    """
    Return a new list with each number squared.

    Args:
        numbers (list): List of numbers

    Returns:
        list: List where each element is squared

    Example:
        >>> square_numbers([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    # TODO: Implement this function
    # Hint: Try a list comprehension!
    squared = [n ** 2 for n in numbers] # n**2 allows to square every number. squared is the list containing these squared numbers
    return squared
    pass


def find_max_min(numbers):
    """
    Find the maximum and minimum values in a list.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)

    Example:
        >>> find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
        (9, 1)
    """
    # TODO: Implement this function
    # You can use max() and min() built-in functions
    max_value = max(numbers) # find the max number of the list numbers
    min_value = min(numbers) # find the min number of the list numbers
    return (max_value, min_value) #return the max and min
    pass


def remove_duplicates(items):
    """
    Remove duplicate items from a list while preserving order.

    Args:
        items (list): List that may contain duplicates

    Returns:
        list: List with duplicates removed

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 4, 3, 5])
        [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    # Hint: You can use a loop and check if item is already in result list
    # Or convert to set and back to list (but this doesn't preserve order)
    result = [] #create an empty list
    for item in items:  # we look at each item in items
        if item not in result:   # check if it's already added
            result.append(item)  #if not, we add it
    return result #return the new list with just one time each different item
    pass


def merge_lists(list1, list2):
    """
    Merge two lists, alternating elements from each.
    If one list is longer, append remaining elements.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        list: Merged list with alternating elements

    Example:
        >>> merge_lists([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge_lists([1, 2], [10, 20, 30, 40])
        [1, 10, 2, 20, 30, 40]
    """
    # TODO: Implement this function
    # Hint: Use a loop with index, handle different lengths
    merged = [] #create a new list
    max_length = max(len(list1), len(list2))

    for i in range(max_length): # take all the elements of the 2 list including the longest one
        if i < len(list1):      #if list1 still has an element, we add it
            merged.append(list1[i])
        if i < len(list2):   #if list2 still has an element, we add it
            merged.append(list2[i])   

    return merged
    pass


def list_statistics(numbers):
    """
    Calculate statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with keys 'sum', 'average', 'count', 'max', 'min'

    Example:
        >>> list_statistics([1, 2, 3, 4, 5])
        {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    """
    if not numbers:
        return None

    # TODO: Implement this function
    # Calculate and return a dictionary with the statistics
    total = sum(numbers) #sum all the elements
    count = len(numbers) #give the number of elements
    avg = total / count #give the average of all the numbers
    maximum = max(numbers) #find the max value
    minimum = min(numbers) #find the min value

    stats = { #cerate the dictionary stats with all these elements inside
        'sum': total,
        'average': avg,
        'count': count,
        'max': maximum,
        'min': minimum
    }

    return stats
    pass


def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size.

    Args:
        items (list): List to split
        chunk_size (int): Size of each chunk

    Returns:
        list: List of lists (chunks)

    Example:
        >>> chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    # TODO: Implement this function
    # Hint: Use list slicing in a loop
    chunks = []
    for i in range(0, len(items), chunk_size): #create a sequence of indices spaced by chunk size
        chunks.append(items[i:i + chunk_size]) # add the following sublist to chunk ; create a sublist of chunk size
    return chunks
    pass


# Test cases
if __name__ == "__main__":
    print("Testing List Operations...")
    print("-" * 50)

    # Test create_number_list
    print("Test 1: create_number_list(1, 5)")
    result = create_number_list(1, 5)
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test filter_even_numbers
    print("Test 2: filter_even_numbers([1, 2, 3, 4, 5, 6])")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"Result: {result}")
    assert result == [2, 4, 6], "Failed!"
    print("✓ Passed\n")

    # Test square_numbers
    print("Test 3: square_numbers([1, 2, 3, 4])")
    result = square_numbers([1, 2, 3, 4])
    print(f"Result: {result}")
    assert result == [1, 4, 9, 16], "Failed!"
    print("✓ Passed\n")

    # Test find_max_min
    print("Test 4: find_max_min([3, 1, 4, 1, 5, 9, 2, 6])")
    result = find_max_min([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Result: {result}")
    assert result == (9, 1), "Failed!"
    print("✓ Passed\n")

    # Test remove_duplicates
    print("Test 5: remove_duplicates([1, 2, 2, 3, 4, 3, 5])")
    result = remove_duplicates([1, 2, 2, 3, 4, 3, 5])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5], "Failed!"
    print("✓ Passed\n")

    # Test merge_lists
    print("Test 6: merge_lists([1, 3, 5], [2, 4, 6])")
    result = merge_lists([1, 3, 5], [2, 4, 6])
    print(f"Result: {result}")
    assert result == [1, 2, 3, 4, 5, 6], "Failed!"
    print("✓ Passed\n")

    # Test list_statistics
    print("Test 7: list_statistics([1, 2, 3, 4, 5])")
    result = list_statistics([1, 2, 3, 4, 5])
    print(f"Result: {result}")
    expected = {'sum': 15, 'average': 3.0, 'count': 5, 'max': 5, 'min': 1}
    assert result == expected, "Failed!"
    print("✓ Passed\n")

    # Test chunk_list
    print("Test 8: chunk_list([1, 2, 3, 4, 5, 6, 7], 3)")
    result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
    print(f"Result: {result}")
    assert result == [[1, 2, 3], [4, 5, 6], [7]], "Failed!"
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Great work!")
