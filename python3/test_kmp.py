import pytest

from kmp import kmp_substr, lps_table


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


@pytest.mark.parametrize(
    ("needle", "haystack", "expected"),
    [
        ("a", "a", 0),
        ("abc", "ababdabc", 5),
        ("a", "b", -1),
        ("abc", "abdabdacf", -1),
    ],
)
def test_kmp_substr(needle: str, haystack: str, expected: int) -> None:
    actual = kmp_substr(needle=needle, haystack=haystack)
    assert actual == expected


@pytest.mark.parametrize(("needle", "haystack"), [("", ""), ("", "hi"), ("hi", "")])
def test_kmp_substr_bad_inputs(needle: str, haystack: str) -> None:
    with pytest.raises(ValueError):
        _ = kmp_substr(needle, haystack)