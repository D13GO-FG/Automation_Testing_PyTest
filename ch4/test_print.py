# pytest test_print.py::test_normal
# pytest -s test_print.py::test_normal  ---> print prints using pytest
# pytest test_print.py::test_fail ---> print default print when fails some test


def test_normal():
    print("\nnormal print")


def test_fail():
    print("\nprint in failing test")
    assert False


def test_disabled(capsys):
    with capsys.disabled():
        print("\ncapsys disabled print")
