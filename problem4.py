"""
Problem 4: Data Persistence with JSON
Learn to use Python modules (imports) and save data to files using JSON.
"""

import json
# Note: json is a built-in Python module for working with JSON data


def save_to_json(data, filename):
    """
    Save data to a JSON file.

    Args:
        data: Python data structure (list, dict, etc.)
        filename (str): Name of file to save to

    Returns:
        bool: True if successful, False if error occurred

    Example:
        >>> data = {'name': 'Alice', 'age': 25}
        >>> save_to_json(data, 'test.json')
        True
    """
    # TODO: Implement this function
    # Steps:
    # 1. Open file in write mode
    # 2. Use json.dump() to write data
    # 3. Return True if successful
    # 4. Use try/except to catch errors and return False

    # Hint:
    # with open(filename, 'w') as f:
    #     json.dump(data, f, indent=2)
    try: #try / except avoid that an error crashed the system
        with open(filename, 'w') as f: #open the file in write mode or create it if it doesn't exist
            json.dump(data, f, indent=2) #write what is in data in the json file with an indent of 2 spaces
        return True #if it works, return true
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
        return False #otherwise, false

    pass


def load_from_json(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): Name of file to load from

    Returns:
        Data from file if successful, None if error occurred

    Example:
        >>> data = load_from_json('test.json')
        >>> data
        {'name': 'Alice', 'age': 25}
    """
    # TODO: Implement this function
    # Steps:
    # 1. Try to open and read the file
    # 2. Use json.load() to parse the data
    # 3. Return the data
    # 4. If file not found or error, return None

    # Hint:
    # with open(filename, 'r') as f:
    #     return json.load(f)
    try: # try / except avoids the error if the file doesn't exist or is not in json, etc...
        with open(filename, 'r') as f: #open the file in read mode
            data = json.load(f) #convert the json file in python object
        return data
    except Exception as e: #if there is an error, return None
        print(f"Error loading {filename}: {e}")
        return None
    pass


def save_contacts_to_file(contacts, filename="contacts.json"):
    """
    Save a list of contacts to a JSON file.

    Args:
        contacts (list): List of contact dictionaries
        filename (str): File to save to (default: contacts.json)

    Returns:
        bool: True if successful, False otherwise
    """
    # TODO: Implement this function
    # Use save_to_json() to save the contacts list
    return save_to_json(contacts, filename) #use the function to save the list contacts in a file json
    pass


def load_contacts_from_file(filename="contacts.json"):
    """
    Load contacts from a JSON file.

    Args:
        filename (str): File to load from (default: contacts.json)

    Returns:
        list: List of contacts, or empty list if file doesn't exist
    """
    # TODO: Implement this function
    # Use load_from_json() to load contacts
    # If None is returned (file not found), return empty list []
    data = load_from_json(filename) #call the function to put the datas in python or none if there is an error
    if data is None:
        return [] #if it's None, we return an empty list
    return data
    pass


def append_contact_to_file(contact, filename="contacts.json"):
    """
    Load existing contacts, add a new contact, and save back to file.

    Args:
        contact (dict): Contact dictionary to add
        filename (str): File to use

    Returns:
        bool: True if successful
    """
    # TODO: Implement this function
    # Steps:
    # 1. Load existing contacts
    contacts = load_contacts_from_file(filename) #take the existing contacts list or an empty list if it doesn't exist
    # 2. Add new contact to list
    contacts.append(contact) #add the new contact to the list
    # 3. Save updated list back to file
    return save_contacts_to_file(contacts, filename) #rewrite the json file with the updated version
    pass


def backup_file(source_filename, backup_filename):
    """
    Create a backup copy of a file.

    Args:
        source_filename (str): Original file
        backup_filename (str): Backup file name

    Returns:
        bool: True if successful
    """
    # TODO: Implement this function
    # Load data from source_filename and save to backup_filename
    data = load_from_json(source_filename) #to read what is inside the origin file
    if data is None: #if the file doesn't exist or is invalid (none)
        print(f"Error: Could not load {source_filename}")
        return False
    return save_to_json(data, backup_filename) #if everything is ok, we call save_to_json
    pass


def get_file_stats(filename):
    """
    Get statistics about a JSON file.

    Args:
        filename (str): File to analyze

    Returns:
        dict or None: Dictionary with keys:
            - 'exists': bool
            - 'type': 'list' or 'dict' or 'other'
            - 'count': number of items (if list) or keys (if dict)
            - 'size_bytes': file size in bytes

    Example:
        >>> get_file_stats('contacts.json')
        {'exists': True, 'type': 'list', 'count': 5, 'size_bytes': 1234}
    """
    # TODO: Implement this function
    # Use os.path.exists() and os.path.getsize() (need to import os)
    # Load the JSON data and determine its type
    import os

    # Check if file exists
    # Get file size
    # Load data and check type
    # Return statistics dictionary

    stats = { #we create a dictionary stats with the needed values
        'exists': False,
        'type': 'other',
        'count': 0,
        'size_bytes': 0
    }

    if not os.path.exists(filename): #verify if the file exists
        return stats  #if it doesn't exist, return stats

    stats['exists'] = True
    stats['size_bytes'] = os.path.getsize(filename) #update file's size in terms of bytes

    data = load_from_json(filename) #load the json's datas

    if data is None: #if it can't return stats
        return stats

    if isinstance(data, list): #if it succeeds and is a list, we put the type list and number of elements
        stats['type'] = 'list'
        stats['count'] = len(data)
    elif isinstance(data, dict): #if it succeeds and is a dictionary, we put the type dictionary and number of keys
        stats['type'] = 'dict'
        stats['count'] = len(data.keys())
    else: #if it succeeds and is something else, we put the type other
        stats['type'] = 'other'

    return stats
    pass


def merge_json_files(file1, file2, output_file):
    """
    Merge two JSON files containing lists.

    Args:
        file1 (str): First file
        file2 (str): Second file
        output_file (str): Output file

    Returns:
        bool: True if successful

    Example:
        If file1.json has [1, 2, 3] and file2.json has [4, 5],
        output_file.json will have [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    # Steps:
    # 1. Load data from both files
    # 2. If both are lists, combine them
    # 3. Save combined list to output_file
    # 4. Handle cases where files might not exist
    data1 = load_from_json(file1)
    data2 = load_from_json(file2) #loading the datas from both files
    if data1 is None:
        data1 = []
    if data2 is None:
        data2 = [] #if a file doesn't exist or is empty, replace it by an empty list
    if not isinstance(data1, list) or not isinstance(data2, list): #verify that both are lists
        print("Error: Both files must contain JSON lists.") #otherwise, we print an error message
        return False
    merged_data = data1 + data2 #merge both of the lists
    return save_to_json(merged_data, output_file) #we save the result in output_file using function
    pass


def search_json_file(filename, key, value):
    """
    Search a JSON file (containing a list of dicts) for items matching a key-value pair.

    Args:
        filename (str): JSON file to search
        key (str): Key to search for
        value: Value to match

    Returns:
        list: List of matching items

    Example:
        If file has [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        search_json_file('data.json', 'name', 'Alice')
        returns [{'name': 'Alice', 'age': 25}]
    """
    # TODO: Implement this function
    # Load data and filter items where item[key] == value
    data = load_from_json(filename) #read what is inside the file
    if not isinstance(data, list): #verify that the file exists and contains a list
        return [] #otherwise returns an empty list
    matches = [item for item in data if isinstance(item, dict) and item.get(key) == value] #comprehension list that take the value associated to the key in the dictionary
    return matches
    pass


# Test cases
if __name__ == "__main__":
    print("Testing JSON File Operations...")
    print("-" * 50)

    # Test 1: save_to_json and load_from_json
    print("Test 1: save_to_json and load_from_json")
    test_data = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
    save_to_json(test_data, 'test_data.json')
    loaded_data = load_from_json('test_data.json')
    print(f"Saved and loaded: {loaded_data}")
    assert loaded_data == test_data
    print("✓ Passed\n")

    # Test 2: save_contacts_to_file and load_contacts_from_file
    print("Test 2: save and load contacts")
    contacts = [
        {'name': 'Alice', 'phone': '555-0001', 'email': 'alice@email.com'},
        {'name': 'Bob', 'phone': '555-0002', 'email': 'bob@email.com'}
    ]
    save_contacts_to_file(contacts, 'test_contacts.json')
    loaded_contacts = load_contacts_from_file('test_contacts.json')
    print(f"Loaded {len(loaded_contacts)} contacts")
    assert len(loaded_contacts) == 2
    assert loaded_contacts[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Test 3: append_contact_to_file
    print("Test 3: append_contact_to_file")
    new_contact = {'name': 'Charlie', 'phone': '555-0003', 'email': 'charlie@email.com'}
    append_contact_to_file(new_contact, 'test_contacts.json')
    contacts = load_contacts_from_file('test_contacts.json')
    print(f"After append: {len(contacts)} contacts")
    assert len(contacts) == 3
    print("✓ Passed\n")

    # Test 4: backup_file
    print("Test 4: backup_file")
    backup_file('test_contacts.json', 'test_contacts_backup.json')
    backup_data = load_from_json('test_contacts_backup.json')
    print(f"Backup created with {len(backup_data)} items")
    assert len(backup_data) == 3
    print("✓ Passed\n")

    # Test 5: get_file_stats
    print("Test 5: get_file_stats")
    stats = get_file_stats('test_contacts.json')
    print(f"File stats: {stats}")
    assert stats is not None
    assert stats['exists'] == True
    assert stats['type'] == 'list'
    assert stats['count'] == 3
    print("✓ Passed\n")

    # Test 6: merge_json_files
    print("Test 6: merge_json_files")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    save_to_json(list1, 'list1.json')
    save_to_json(list2, 'list2.json')
    merge_json_files('list1.json', 'list2.json', 'merged.json')
    merged = load_from_json('merged.json')
    print(f"Merged list: {merged}")
    assert merged == [1, 2, 3, 4, 5, 6]
    print("✓ Passed\n")

    # Test 7: search_json_file
    print("Test 7: search_json_file")
    results = search_json_file('test_contacts.json', 'name', 'Alice')
    print(f"Search results: {results}")
    assert len(results) == 1
    assert results[0]['name'] == 'Alice'
    print("✓ Passed\n")

    # Cleanup
    print("Cleaning up test files...")
    import os
    for file in ['test_data.json', 'test_contacts.json', 'test_contacts_backup.json',
                 'list1.json', 'list2.json', 'merged.json']:
        if os.path.exists(file):
            os.remove(file)
    print("✓ Cleaned up\n")

    print("=" * 50)
    print("All tests passed! You've mastered JSON file operations!")
