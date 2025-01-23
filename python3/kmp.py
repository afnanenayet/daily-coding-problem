"""
The KMP substring matching algorithm. Trying to derive this from scratch.
"""


def lps_table(needle: str) -> list[int]:
    """
    Construct the lookup table for the longest prefix that is also a suffix (LPS) for every substring
    of `needle`.

    Args:
        needle: The string that you want to search for matches within a larger string.

    Returns:
        An array that has the length of the LPS for each substring `needle[0..i]` at each index `i`.
    """
    if len(needle) == 0:
        return []

    # lps[i] = length of longest prefix that is also a suffix in needle[:i]
    lps = [0] * len(needle)

    # There is no LPS of an empty string.
    lps[0] = -1

    # Index in the needle that we use to traverse forward
    i = 1

    # zero based index in the needle of the next character of the current candidate substring
    lp_i = 0

    # For each index in the needle, we try to build up the LPS. If we fail to match,
    # then we go to the previous prefix until we hit an index of -1.
    while i < len(needle):
        # We have a match, we can just continue the LPS chain we have been building
        if needle[i] == needle[lp_i]:
            lp_i += 1
            lps[i] = lp_i
            i += 1
        # Mismatch. We can't have a valid LPS of length `curr_lps + 1`. To avoid redoing
        # work, we keep jumping to the last LPS from the previous string to see if we can
        # build up one of the shorter LPS' we discovered. This way, we don't have to scan
        # from the very beginning of the string all over again and redo work.
        elif lp_i > 0:
            lp_i = lps[lp_i - 1]
        else:
            lp_i = 0
            i += 1
    return lps


def kmp_substr(needle: str, haystack: str) -> int:
    """
    Uses the KMP string matching algorithm to find the starting index where `needle`
    is in haystack (if `haystack` contains `needle`).

    Args:
        needle: The substring to search for within `haystack`. This must not be an empty string.
        haystack: The string to search. This must not be an empty string.

    Returns:
        The start index of where `needle` is in `haystack`. If the substring is not found,
        this will return `-1`.
    """
    if len(haystack) == 0:
        raise ValueError("The haystack must not be an empty string")

    # Not sure if this makes sense semantically. We made an arbitrary choice here.
    if len(needle) == 0:
        raise ValueError("The needle must not be an empty string")

    lps = lps_table(needle)

    # Basic sanity checks
    assert len(lps) == len(needle)
    assert lps[0] == -1

    # Now we maintain a sliding window with two pointers. Best case scenario is that
    # we build up matches, so we can move up the index of the haystack and needle simultaneously.
    # If we have a mismatch, we can slide over the needle based on how many characters have already
    # matched up. We use the LPS table to avoid redoing work because it can tell us exactly how many
    # characters still match as we slide the haystack pointer forward.

    h_i = 0  # Pointer in the haystack
    n_i = 0  # Pointer to the current position in the needle

    while h_i < len(haystack):
        # import pdb; pdb.set_trace()
        while (
            n_i < len(needle) and h_i < len(haystack) and needle[n_i] == haystack[h_i]
        ):
            n_i += 1
            h_i += 1

        # We matched the entire needle. Return the start index in the haystack.
        if n_i == len(needle):
            return h_i - len(needle)

        # If we get here, that means we've run into a mismatch. We need to slide the window
        # up so we don't look at redundant characters in the needle that already match up.
        while n_i >= 0 and needle[n_i] != haystack[h_i]:
            n_i = lps[n_i]

        # We have the sentinel value, -1, at the beginning of the string. If `n_i` ends up at -1,
        # that means we've basically exhausted the search of the needle and none of the characters
        # between the needle and the haystack match up to the current index `h_i`, so we increment `h_i`.
        # This is equivalent to moving the sliding window of the needle up all the way, and we try looking
        # for matches again in the next iteration of the loop.
        if n_i < 0:
            h_i += 1
            n_i = 0
    return -1
