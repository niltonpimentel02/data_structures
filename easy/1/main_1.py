from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_to_index = dict()
    nums_count = len(nums)

    for current_index in range(nums_count):
        complement = target - nums[current_index]
        if complement in num_to_index:
            return [num_to_index[complement], current_index]
        num_to_index[nums[current_index]] = current_index

    return []
