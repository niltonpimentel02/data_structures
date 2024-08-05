# Version 1
# def find_duplicates(numbers):
#     duplicates = []
#     for i in numbers:
#         if numbers.count(i) > 1:
#             duplicates.append(i)
#     unique_duplicates = list(set(duplicates))
#     return unique_duplicates
from icecream import ic


# Version 2
# def find_duplicates(numbers):
#     duplicates = [i for i in numbers if numbers.count(i) > 1]
#     return list(set(duplicates))

# Version 3
# def find_duplicates(numbers):
#     duplicates = {}
#     for num in numbers:
#         duplicates[num] = duplicates.get(num, 0) + 1
#     duplicates = [num for num, count in duplicates.items() if count > 1]
#     return duplicates

def find_duplicates(numbers: list) -> list:
    """
    Find duplicate numbers in a list and return them as a list.

    Args:
        numbers (List[int]): List of numbers to check for duplicates.

    Returns:
        List[int]: List of duplicate numbers.
    """
    # Create a dictionary to store the count of each number
    duplicates = {}

    # Iterate over each number in the list
    for num in numbers:
        # Get the current count of the number and increment it by 1
        duplicates[num] = duplicates.get(num, 0) + 1

    # Filter the dictionary to get only the numbers with a count greater than 1
    duplicates = [num for num, count in duplicates.items() if count > 1]

    # Return the list of duplicate numbers
    return duplicates


ic(find_duplicates([1, 2, 3, 4, 5]))
ic(find_duplicates([1, 1, 2, 2, 3]))
ic(find_duplicates([1, 1, 1, 1, 1]))
ic(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
ic(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
ic(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
ic(find_duplicates([]))
