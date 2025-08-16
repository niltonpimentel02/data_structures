from main_1 import two_sum

class TestTwoSum:
    def test_two_sum_case_0(self):
        content = [2, 7, 11, 15]
        target_sum = 9
        expected = [0, 1]
        assert two_sum(content, target_sum) == expected
