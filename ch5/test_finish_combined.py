from pathlib import Path
from tempfile import TemporaryDirectory
from cards import Card
import pytest
import cards


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def test_finish(cards_db):
    for c in [
        Card("write a book", state="done"),
        Card("second edition", state="in prog"),
        Card("create a course", state="todo"),
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
