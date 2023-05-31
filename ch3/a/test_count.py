import cards

# pytest --setup-show test_count.py

# Finding Where Fixtures Are Defined
# pytest --fixtures -v
# pytest --fixtures-per-test test_count.py::test_empty


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2
