from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards
from cards import Card, InvalidCardId

# pytest -v -m exception
# pytest -v -m smoke
# pytest -v -m finish

pytestmark = pytest.mark.finish


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.mark.smoke
class TestFinish:
    def test_finish_from_todo(self, cards_db):
        i = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"

    def test_finish_from_in_prog(self, cards_db):
        i = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"

    def test_finish_from_done(self, cards_db):
        i = cards_db.add_card(Card("foo", state="done"))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == "done"


@pytest.mark.parametrize("start_state", [
    "todo",
    pytest.param("in prog", marks=pytest.mark.smoke),
    "done",
])
def test_finish_func(cards_db, start_state):
    i = cards_db.add_card(Card("foo", state=start_state))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"


@pytest.fixture(
    params=[
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]
)
def start_state_fixture(request):
    return request.param


def test_finish_fix(cards_db, start_state_fixture):
    i = cards_db.add_card(Card("foo", state=start_state_fixture))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"


@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(cards_db):
    i = 123  # any number will do, db is empty
    with pytest.raises(InvalidCardId):
        cards_db.finish(i)
