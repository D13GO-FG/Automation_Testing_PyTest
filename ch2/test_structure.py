from cards import Card

"""
Given/Arrange—A starting state. This is where you set up data or the environment to get ready for the action.
When/Act—Some action is performed. This is the focus of the test—the behavior we are trying to make sure is working right.
Then/Assert—Some expected result or end state should happen. At the end of the test, we make sure the action resulted in the expected behavior.
"""


def test_to_dict():
    # GIVEN/ARRANGE a Card object with known contents
    c1 = Card("something", "Diego", "todo", 123)
    # WHEN/ACT we call to_dict() on the object
    c2 = c1.to_dict()
    # THEN/ASSERT the result will be a dictionary with known content
    c2_expected = {
        "summary": "something",
        "owner": "Diego",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected
