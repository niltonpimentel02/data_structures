from typing import List


# def contains_duplicate(nums: List[int]) -> bool:
#     duplicates = []
#     for num in nums:
#         if num in duplicates:
#             return True
#         duplicates.append(num)
#     return False


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
