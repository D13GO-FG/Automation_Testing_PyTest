from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards
from cards import Card, InvalidCardId


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_start(cards_db):
    """
    start changes state from "todo" to "in prog"
    """
    i = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"


def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    any_number = 123  # any number will be invalid, db is empty
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)
