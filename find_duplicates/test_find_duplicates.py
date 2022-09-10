from .find_duplicates import find_duplicates

class TestFindDuplicates:
    def test_find_duplicates_0(self):
        content = [1, 2, 3, 4]
        expected = []
        assert find_duplicates(content) == expected

    def test_find_duplicates_1(self):
        content = [1, 2, 2, 3, 4]
        expected = [2]
        assert find_duplicates(content) == expected

    def test_find_duplicates_2(self):
        content = [1, 2, 2, 3, 4, 4]
        expected = [2, 4]
        assert find_duplicates(content) == expected

    def test_find_duplicates_3(self):
        content = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
        expected = [2, 4, 5]
        assert find_duplicates(content) == expected

    def test_find_duplicates_4(self):
        content = [1, 2, 4, 2, 3, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5]
        expected = [2, 4, 5]
        assert find_duplicates(content) == expected
