// Starting from 0 on a number line, you would like to make a series of jumps
// that lead to the integer N. On the ith jump, you may move exactly i places to
// the left or right. Find a path with the fewest number of jumps required to
// get from 0 to N.

#include "pch.hpp"

namespace p579 {
// Get the sum of a series from 1..n
unsigned int series_sum(unsigned int n) { return n * (n + 1) / 2; }

// Calculate the number of jumps that lead to the integer `n`
unsigned int jumps(int n) {
    unsigned int target = abs(n);
    unsigned int ans = 0;

    while (series_sum(ans) < n || (series_sum(ans) - target & 1)) {
        ans++;
    }
    return ans;
}

TEST_CASE("0 jumps", "[579]") { REQUIRE(jumps(0) == 0); }
}; // namespace p579
