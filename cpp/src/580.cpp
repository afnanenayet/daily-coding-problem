// Given a binary tree, find a minimum path sum from root to a leaf.
// For example, the minimum path in this tree is [10, 5, 1, -1], which has
// sum 15.
//  10
// /  \
// 5    5
//  \     \
//   2    1
//       /
//     -1

#include "binary_tree_node.hpp"
#include "pch.hpp"
#include <memory>

namespace p580 {
// Calculate the minimum path sum from some root to a leaf
//
// This method calculates the min path sum recursively
template <typename T> T min_path_sum(BinaryTreeNode<T> *node) {
    if (node == nullptr) {
        return 0;
    }
    unsigned int left_sum = min_path_sum(node->left);
    unsigned int right_sum = min_path_sum(node->right);
    return std::min(left_sum, right_sum) + node->value;
}

TEST_CASE("[10, 5, 1, -1]", "[580]") {
    // I know `new` is bad practice, but it's a test so whatever
    auto tree = new BinaryTreeNode<int>(
        10, new BinaryTreeNode<int>(5, nullptr, new BinaryTreeNode<int>(2)),
        new BinaryTreeNode<int>(
            5, nullptr,
            new BinaryTreeNode<int>(1, new BinaryTreeNode<int>(-1), nullptr)));
    REQUIRE(min_path_sum(tree) == 15);
}
}; // namespace p580
