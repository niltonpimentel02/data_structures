# Version 1
# def find_duplicates(numbers):
#     duplicates = []
#     for i in numbers:
#         if numbers.count(i) > 1:
#             duplicates.append(i)
#     unique_duplicates = list(set(duplicates))
#     return unique_duplicates

# Version 2
def find_duplicates(numbers):
    duplicates = [i for i in numbers if numbers.count(i) > 1]
    return list(set(duplicates))
