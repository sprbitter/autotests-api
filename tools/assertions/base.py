from typing import Any


def assert_status_code(actual: int, expected: int):
    assert actual == expected, (
        "Incorrect status code. Expected {}, but got {}".format(expected, actual)
    )


def assert_equal(actual: Any, expected: Any, name: str) -> None:
    assert actual == expected, (
        "incorrect value: {}. Expected {}, but got {}".format(name, expected, actual))
