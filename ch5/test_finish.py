from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
from cards import Card
import cards


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second edition", state="in prog"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card("write a book", state="done"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card("create a course", state="todo"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
