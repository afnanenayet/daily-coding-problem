/*
Given an N by M matrix consisting only of 1's and 0's, find the largest
rectangle containing only 1's and return its area.
*/

#include "pch.hpp"

namespace p585 {

// Return the maximum rectangle given a one-dimensional histogram
//
// We use an O(n) algorithm to solve this problem
template <size_t N> auto max_rect_histogram(const std::array<int, N> &input) {
    // The stack holds the index of the elements that are less than the current
    // element. The invariant here is that the stack must be made of elements
    // that are ascending (the elements are always inserted in ascending order).
    std::stack<int> s;
    s.push(0);

    auto current_max = 0;
    std::vector hist(input.begin(), input.end()); // CTAD FTW

    // Add sentinel values for the left and right boundaries of the histogram
    hist.insert(hist.begin(), -1);
    hist.push_back(-1);

    // We loop through each element of the histogram
    //
    // If the top of the stack is holding an element that is greater than the
    // current element in the histogram, then we will find the largest possible
    // area of a rectangle with a corresponding height. We pop that element off
    // the stack to find the next element in the histogram that has a height
    // less than the `height` we've assigned to the rectangle. This is why we
    // only add to the stack in ascending order.
    //
    // We keep doing this until the top of the stack is less than the current
    // element, so we try out every possible intermediate height to the left of
    // the current element that is greater than the current element.
    //
    // Finally, we push the current element to the stack.
    for (auto i = 0; i < hist.size(); i++) {
        // NOTE: we don't have to check if the stack is empty, because -1 is an
        // illegal height and we will never have an instance where `hist[i] <
        // -1`.
        while (hist[i] < hist[s.top()]) {
            const auto height = hist[s.top()];
            s.pop();
            const auto top_idx = s.top();
            const auto width = i - top_idx - 1;
            current_max = std::max(current_max, height * width);
        }
        s.push(i);
    }
    return current_max;
}

// Given a 2D matrix, return the area of the largest rectangle inside the matrix
template <size_t M, size_t N>
auto largest_rectangle(const std::array<std::array<int, N>, M> &grid) {
    // NOTE: we don't have to worry about checking for 0 sized arrays because
    // they're illegal in C++, so we can skip that check here

    // dp[i][j] returns the largest rectangle that has its bottom right corner
    // anchored to grid[i][j]
    std::array<int, N> hist{};

    // The maximum area seen so far given the rows we have examined
    auto max_area = 0;

    for (const auto &row : grid) {
        for (auto i = 0; i < N; i++) {
            // If we have a zero, then the rectangle can't continue, so zero it
            // out. Otherwise we keep incrementing the histogram.
            if (row[i] == 0) {
                hist[i] = 0;
            } else {
                hist[i] += row[i];
            }
        }
        // Calculate the maximum area of the accumulated histogram and
        // compare it to the previous max, updating if necessary.
        max_area = std::max(max_area, max_rect_histogram(hist));
    }
    return max_area;
}

TEST_CASE("max rectangle histogram", "[585]") {
    {
        std::array input = {0};
        REQUIRE(max_rect_histogram(input) == 0);
    }
    {
        std::array input = {1};
        REQUIRE(max_rect_histogram(input) == 1);
    }
    {
        std::array input = {1, 1, 1, 1};
        REQUIRE(max_rect_histogram(input) == 4);
    }
}

TEST_CASE("input example", "[585]") {
    std::array<std::array<int, 4>, 4> grid{
        {{1, 0, 0, 0}, {1, 0, 1, 1}, {1, 0, 1, 1}, {0, 1, 0, 0}}};
    REQUIRE(largest_rectangle(grid) == 4);
}
}; // namespace p585
