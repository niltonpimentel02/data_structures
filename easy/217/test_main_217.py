from main_217 import contains_duplicate


class TestContainsDuplicate:
    def test_contains_duplicate_case_0(self):
        content = [1, 2, 3, 1]
        expected = True
        assert contains_duplicate(content) == expected

    def test_contains_duplicate_case_1(self):
        content = [1, 2, 3, 4]
        expected = False
        assert contains_duplicate(content) == expected

    def test_contains_duplicate_case_2(self):
        content = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        assert contains_duplicate(content) == expected

    def test_contains_duplicate_case_3(self):
        content = []
        expected = False
        assert contains_duplicate(content) == expected

    def test_contains_duplicate_case_4(self):
        content = [1]
        expected = False
        assert contains_duplicate(content) == expected
