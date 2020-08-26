/*
You are given a 2-d matrix where each cell represents number of coins in that
cell. Assuming we start at matrix[0][0], and can only move right or down, find
the maximum number of coins you can collect by the bottom right corner.
*/

#include "pch.hpp"

namespace p583 {

// A type alias for a 2D matrix
template <typename T, int X, int Y>
using Matrix2D = std::array<std::array<T, Y>, X>;

using uint = unsigned int;

// Find the path with the maximum number of coins starting from the top right
// corner and going to the bottom right corner
//
// We use a 2D grid to track the maximum sum for each partial path. We define
// this problem in terms of subproblems, where we can always deduce the maximum
// path as the maximum of the max path that ends at the cell above or to the
// left of the current cell + the value of the current cell.
template <uint X, uint Y> uint max_coins(const uint (&grid)[X][Y]) {
    // dp[i][j] returns the maximum number of coins that you can collect going
    // from [0][0] to [i][j], moving only right or down
    Matrix2D<uint, X, Y> dp{};

    // Initialize the DP grid by setting the max for the top and left edges
    for (int i = 0; i < dp.size(); i++) {
        dp[i][0] = grid[i][0];
    }

    for (int j = 0; j < dp.size(); j++) {
        dp[0][j] = grid[0][j];
    }

    // For each element in the grid, check to see which path leads to a maximum,
    // the path that ends at one cell above or to the left, and then add the
    // value of the coin on the current grid
    for (int i = 1; i < dp.size(); i++) {
        for (int j = 1; j < dp[i].size(); j++) {
            dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
        }
    }
    return dp.back().back();
}

TEST_CASE("given example", "[583]") {
    REQUIRE(max_coins({
                {0, 3, 1, 1},
                {2, 0, 0, 4},
                {1, 5, 3, 1},
            }) == 12);
    REQUIRE(max_coins({{0}}) == 0);
}
}; // namespace p583
