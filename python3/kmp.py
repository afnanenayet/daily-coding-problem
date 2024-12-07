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

    lps = [0] * len(needle)

    # There is no LPS of an empty string.
    lps[0] = -1

    # Index in the needle that we use to traverse forward
    i = 1

    # Index of the candidate prefix that we're trying to build a suffix on
    lp_i = 0
    curr_lps = 0

    # For each index in the needle, we try to build up the LPS. If we fail to match,
    # then we go to the previous prefix until we hit an index of -1.
    while i < len(needle):
        c = needle[i]
        # We have a match, we can just continue the LPS chain we have been building
        if c == needle[lp_i]:
            curr_lps += 1
            lp_i += 1
        # Mismatch. We can't have a valid LPS of length `curr_lps + 1`. To avoid redoing
        # work, we keep jumping to the last LPS from the previous string to see if we can
        # build up one of the shorter LPS' we discovered. This way, we don't have to scan
        # from the very beginning of the string all over again and redo work.
        else:
            while lps[lp_i] > 0 and c != needle[lp_i]:
                # Go to the previous LPS, and see if we can continue the chain
                lp_i = lps[lp_i]

            # Max is here to zero out the length if we went to the beginning and there's no
            # possible lps.
            curr_lps = max(0, lps[lp_i])

        lps[i] = curr_lps
        i += 1
    return lps
