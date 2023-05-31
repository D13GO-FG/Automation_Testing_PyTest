import cards

# pytest -v --tb=line test_count.py test_three.py
# Database problem because previous test cases created more instances that expected, so it's requiere delete previous interactions.


def test_three(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    cards_db.add_card(cards.Card("third"))
    assert cards_db.count() == 3
