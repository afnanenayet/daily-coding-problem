/*
Let X be a set of n intervals on the real line. We say that a set of points P
"stabs" X if every interval in X contains at least one point in P. Compute the
smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should
return [4, 9].
 */

#include "pch.hpp"

namespace p582 {
// A struct representing some interval
class Interval {
  public:
    int start;
    int end;

    bool operator==(const Interval &other) const {
        return this->start == other.start && this->end == other.end;
    }
};

std::ostream &operator<<(std::ostream &os, Interval const &value) {
    os << fmt::format("({:d}, {:d})", value.start, value.end);
    return os;
}

// Compute the minimal interval that is "stabbed" by all of the input intervals
//
// This is O(n) space and O(nlogn) time. You could reduce memory usage by
// sorting in-place, but I generally assume that the inputs are immutable.
Interval minimal_interval(const std::vector<Interval> &input_list) {
    if (input_list.empty()) {
        throw std::invalid_argument("Input list must not be empty");
    }
    auto intervals = input_list;

    // First, we sort the intervals by their endpoints
    auto cmp = [](const Interval &a, const Interval &b) {
        return a.end < b.end;
    };
    std::sort(intervals.begin(), intervals.end(), cmp);
    auto stab_interval =
        Interval{intervals.begin()->end, intervals.begin()->end};

    // We extend the end of the interval by the start value of the next interval
    // if the next interval isn't already stabbed by our stab interval. Since
    // we've sorted by endpoint, we know that the endpoint of the stab interval
    // is less than or equal to the endpoint of the current interval, and the
    // minimal interval we need to stab the current interval is to extend the
    // stab interval minimally so that it covers the interval. If the current
    // stab interval has an endpoint that is greater than the current interval,
    // then the current interval has already been stabbed.
    for (const auto &interval : intervals) {
        stab_interval.end = std::max(stab_interval.end, interval.start);
    }
    return stab_interval;
}

TEST_CASE("misc examples", "[582]") {
    REQUIRE(minimal_interval({{1, 4}, {4, 5}, {7, 9}, {9, 12}}) ==
            Interval{4, 9});
    REQUIRE(minimal_interval({{0, 4}, {1, 2}, {-3, 7}}) == Interval{2, 2});
}
}; // namespace p582
