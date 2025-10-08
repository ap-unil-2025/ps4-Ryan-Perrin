"""
Problem 2: Dictionary Operations and Nested Structures
Practice working with Python dictionaries - creating, accessing, modifying, and nesting them.
"""


def create_student_record(name, age, major, gpa):
    """
    Create a student record as a dictionary.

    Args:
        name (str): Student name
        age (int): Student age
        major (str): Student major
        gpa (float): Student GPA

    Returns:
        dict: Student record with keys 'name', 'age', 'major', 'gpa'

    Example:
        >>> create_student_record("Alice", 20, "Computer Science", 3.8)
        {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'gpa': 3.8}
    """
    # TODO: Implement this function
    # Return a dictionary with the provided information
    student = { # create a dictionary with the informations requested
        'name': name,
        'age': age,
        'major': major,
        'gpa': gpa
    }
    return student
    pass


def get_value_safely(dictionary, key, default=None):
    """
    Get a value from a dictionary safely, returning default if key doesn't exist.

    Args:
        dictionary (dict): The dictionary to search
        key: The key to look for
        default: Value to return if key not found

    Returns:
        The value if key exists, otherwise default

    Example:
        >>> d = {'a': 1, 'b': 2}
        >>> get_value_safely(d, 'a')
        1
        >>> get_value_safely(d, 'c', 'Not found')
        'Not found'
    """
    # TODO: Implement this function
    # Hint: Use the .get() method or check if key in dictionary
    return dictionary.get(key, default) #look for a key; if it exists, returns it, otherwise returns default
    pass


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If keys conflict, dict2's values take precedence.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Merged dictionary

    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    # TODO: Implement this function
    # Create a new dictionary with items from both
    merged = dict1.copy() #create a copy of dictionary 1 to not modify it

    merged.update(dict2) #add all the values of dict2 in merged

    return merged #return the combined dictionary
    pass

import string
def count_word_frequency(text):
    """
    Count the frequency of each word in a text string.
    Convert to lowercase and ignore punctuation.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary mapping each word to its frequency

    Example:
        >>> count_word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    # TODO: Implement this function
    # Steps:
    # 1. Convert text to lowercase
    text = text.lower()
    # 2. Remove punctuation (you can use .replace() or import string)
    for punct in string.punctuation:
        text = text.replace(punct, "")
    # 3. Split into words
    words = text.split()
    # 4. Count each word's frequency
    freq = {}
    for word in words: 
        if word in freq:
            freq[word] += 1 #counts how many times a word appears
        else:
            freq[word] = 1

    return freq
    pass


def invert_dictionary(dictionary):
    """
    Invert a dictionary (swap keys and values).
    Assume all values are unique.

    Args:
        dictionary (dict): Dictionary to invert

    Returns:
        dict: Inverted dictionary

    Example:
        >>> invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        {1: 'a', 2: 'b', 3: 'c'}
    """
    # TODO: Implement this function
    # Create a new dictionary with values as keys and keys as values
    inverted = {value: key for key, value in dictionary.items()} #create a new dictionary where each key becomes the value and each value becomes the key
    return inverted
    pass


def filter_dictionary(dictionary, keys_to_keep):
    """
    Create a new dictionary with only the specified keys.

    Args:
        dictionary (dict): Source dictionary
        keys_to_keep (list): List of keys to keep

    Returns:
        dict: Filtered dictionary

    Example:
        >>> filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
        {'a': 1, 'c': 3}
    """
    # TODO: Implement this function
    # Loop through keys_to_keep and add them to result if they exist
    filtered = {} #create a new empty dictionary
    for key in keys_to_keep: #we look at the list containing the keys to keep
        if key in dictionary: #for each key if it is in dictionary, we copy it with its value
            filtered[key] = dictionary[key]
    return filtered
    pass


def group_by_first_letter(words):
    """
    Group words by their first letter.

    Args:
        words (list): List of words

    Returns:
        dict: Dictionary where keys are first letters, values are lists of words

    Example:
        >>> group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    """
    # TODO: Implement this function
    # For each word:
    #   - Get first letter
    #   - Add word to the list for that letter
    # Hint: Use .setdefault() or check if key exists
    grouped = {}
    for word in words:
        first_letter = word[0].lower()  # word[0] to take the first letter and lower to make it small character to uniform
        grouped.setdefault(first_letter, []).append(word) #create an empty list if the key doesn't exist yet and then add the word to the good list
    return grouped
    pass


def calculate_grades_average(students):
    """
    Calculate the average grade for each student.

    Args:
        students (dict): Dictionary where keys are student names,
                        values are lists of grades

    Returns:
        dict: Dictionary where keys are student names,
              values are average grades (rounded to 2 decimals)

    Example:
        >>> calculate_grades_average({
        ...     'Alice': [90, 85, 88],
        ...     'Bob': [75, 80, 78]
        ... })
        {'Alice': 87.67, 'Bob': 77.67}
    """
    # TODO: Implement this function
    # For each student, calculate average of their grades
    # Hint: sum(grades) / len(grades)
    averages = {}
    for student, grades in students.items(): #in order to see all the keys (names) and appropriated values (grades)
        if grades:  # to not divide by 0
            avg = round(sum(grades) / len(grades), 2) #calculate the average and then round to 2 decimals
        else:
            avg = 0.0
        averages[student] = avg #stock each averaged grade in a new dictionary averages
    return averages
    pass


def nested_dict_access(data, keys):
    """
    Access a nested dictionary using a list of keys.
    Return None if any key doesn't exist.

    Args:
        data (dict): Nested dictionary
        keys (list): List of keys to traverse

    Returns:
        Value at the nested location, or None if not found

    Example:
        >>> data = {'a': {'b': {'c': 123}}}
        >>> nested_dict_access(data, ['a', 'b', 'c'])
        123
        >>> nested_dict_access(data, ['a', 'x'])
        None
    """
    # TODO: Implement this function
    # Start with data, then traverse using each key
    # Return None if any key is missing
    current = data #we create a variable that reprensents where we are in the dictionary
    for key in keys: #we look at each key existing
        if isinstance(current, dict) and key in current: #look if current is really a dictionnary and if a key exists in the dictionary
            current = current[key]   #go down one level
        else:
            return None              #if we can not find the key, we stop there
    return current
    pass


# Test cases
if __name__ == "__main__":
    print("Testing Dictionary Operations...")
    print("-" * 50)

    # Test create_student_record
    print("Test 1: create_student_record")
    result = create_student_record("Alice", 20, "CS", 3.8)
    print(f"Result: {result}")
    assert result == {'name': 'Alice', 'age': 20, 'major': 'CS', 'gpa': 3.8}
    print("✓ Passed\n")

    # Test get_value_safely
    print("Test 2: get_value_safely")
    d = {'a': 1, 'b': 2}
    assert get_value_safely(d, 'a') == 1
    assert get_value_safely(d, 'c', 'Not found') == 'Not found'
    print("✓ Passed\n")

    # Test merge_dictionaries
    print("Test 3: merge_dictionaries")
    result = merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    print(f"Result: {result}")
    assert result == {'a': 1, 'b': 3, 'c': 4}
    print("✓ Passed\n")

    # Test count_word_frequency
    print("Test 4: count_word_frequency")
    result = count_word_frequency("hello world hello")
    print(f"Result: {result}")
    assert result == {'hello': 2, 'world': 1}
    print("✓ Passed\n")

    # Test invert_dictionary
    print("Test 5: invert_dictionary")
    result = invert_dictionary({'a': 1, 'b': 2, 'c': 3})
    print(f"Result: {result}")
    assert result == {1: 'a', 2: 'b', 3: 'c'}
    print("✓ Passed\n")

    # Test filter_dictionary
    print("Test 6: filter_dictionary")
    result = filter_dictionary({'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['a', 'c'])
    print(f"Result: {result}")
    assert result == {'a': 1, 'c': 3}
    print("✓ Passed\n")

    # Test group_by_first_letter
    print("Test 7: group_by_first_letter")
    result = group_by_first_letter(['apple', 'banana', 'apricot', 'blueberry'])
    print(f"Result: {result}")
    assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    print("✓ Passed\n")

    # Test calculate_grades_average
    print("Test 8: calculate_grades_average")
    result = calculate_grades_average({
        'Alice': [90, 85, 88],
        'Bob': [75, 80, 78]
    })
    print(f"Result: {result}")
    assert result == {'Alice': 87.67, 'Bob': 77.67}
    print("✓ Passed\n")

    # Test nested_dict_access
    print("Test 9: nested_dict_access")
    data = {'a': {'b': {'c': 123}}}
    assert nested_dict_access(data, ['a', 'b', 'c']) == 123
    assert nested_dict_access(data, ['a', 'x']) is None
    print("✓ Passed\n")

    print("=" * 50)
    print("All tests passed! Excellent work!")
