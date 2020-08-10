#pragma once

// A module with declarations for a binary tree

// The node of a binary tree
template <typename T> class BinaryTreeNode {
  public:
    BinaryTreeNode<T>(T value, BinaryTreeNode<T> *left,
                      BinaryTreeNode<T> *right)
        : value(value), left(left), right(right) {}

    // A reference to the left child of the node
    BinaryTreeNode<T> *left;

    // A reference to the right child of the node
    BinaryTreeNode<T> *right;

    // The value of the node
    T value;
};
