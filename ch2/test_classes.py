from cards import Card

"""
 pytest ch2/test_classes.py::TestEquality::test_equality
 pytest ch2/test_classes.py::TestEquality
 pytest -v -k TestEq
 pytest -v --tb=no -k equality
 pytest -v --tb=no -k "equality and not equality_fail"  ## logical operation OR and AND
 pytest -v --tb=no -k "(dict or ids) and not TestEquality"
"""


class TestEquality:
    def test_equality(self):
        c1 = Card("something", "Diego", "todo", 123)
        c2 = Card("something", "Diego", "todo", 123)
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 4567)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("completely different", "okken", "done", 123)
        assert c1 != c2
