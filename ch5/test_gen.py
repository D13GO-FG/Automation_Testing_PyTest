from pathlib import Path
from tempfile import TemporaryDirectory
from cards import Card
import pytest
import cards

# pytest -v test_gen.py


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])


def test_finish(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


# ldiego@LAPTOP-KAQJQP02:~/project-python/fundamentals_pytest/ch5$ pytest -v
# pytest -v -k todo  --> run all of the "todo" cases
# pytest -v -k "todo and not(play or create)"  --> if you want to eliminate the test cases with "play" or "create".
# pytest -v "test_func_param.py::test_finish"  --> Select a single test function
# pytest -v "test_func_param.py::test_finish[write a book-done]"  --> select one test case
