#pragma once

#include "pch.hpp"
#include <memory>
#include <optional>

// A module with declarations for a binary tree

// The node of a binary tree
template <typename T> class BinaryTreeNode {
  public:
    // Default constructor
    BinaryTreeNode<T>() : value(T()), left(nullptr), right(nullptr) {}

    // Construct a leaf node with no children
    BinaryTreeNode<T>(T value) : value(value), left(nullptr), right(nullptr) {}

    // Construct a node with a left and right child
    BinaryTreeNode<T>(T value, BinaryTreeNode<T> *left,
                      BinaryTreeNode<T> *right)
        : value(value), left(left), right(right) {}

    BinaryTreeNode<T>(BinaryTreeNode<T> &&other) noexcept
        : value(other.value), left(other.left), right(other.right) {
        other.left = nullptr;
        other.right = nullptr;
    }

    BinaryTreeNode<T>(BinaryTreeNode<T> &other)
        : value(other.value), left(other.left), right(other.right) {}

    BinaryTreeNode<T> &operator=(const BinaryTreeNode<T> &other) {
        return *this = BinaryTreeNode<T>(other);
    }

    BinaryTreeNode<T> &operator=(BinaryTreeNode<T> &&other) noexcept {
        std::swap(left, other.left);
        std::swap(right, other.right);
        std::swap(value, other.value);
        return *this;
    }

    ~BinaryTreeNode<T>() = default;

    // Return whether the node has any children
    //
    // This will return `true` if the node has a left child, a right child, or
    // both.
    bool has_children() const { return left && right; }

    // A reference to the left child of the node
    BinaryTreeNode<T> *left;

    // A reference to the right child of the node
    BinaryTreeNode<T> *right;

    // The value of the node
    T value;
};
