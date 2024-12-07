from kmp import lps_table
import pytest


@pytest.mark.parametrize(
    ("needle", "expected"),
    [
        (
            "",
            [],
        ),
        (
            "aa",
            [-1, 1],
        ),
        (
            "aaa",
            [-1, 1, 2],
        ),
        (
            "abcabc",
            [-1, 0, 0, 1, 2, 3],
        ),
    ],
)
def test_lps_table(needle: str, expected: list[int]) -> None:
    actual = lps_table(needle)
    assert actual == expected
    # Sanity check that the longest listed prefix is also a suffix
    for idx, lps_len in enumerate(actual):
        if lps_len > 0:
            assert needle[:lps_len] == needle[(idx - lps_len + 1) : idx + 1]
