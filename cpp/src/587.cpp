// Given a binary tree, return all paths from the root to leaves

#include "binary_tree_node.hpp"
#include "pch.hpp"

template <typename T> struct VectorHash {
    size_t operator()(const std::vector<T> &v) const {
        auto s = fmt::format("{}", v);
        return std::hash<std::string>{}(s);
    }
};

namespace p587 {

// A path of binary trees
//
// This class is hashable, so it can be used with hashmaps and sets
template <typename T> class BTreePath {
  public:
    std::vector<T> nodes;
};

template <typename T>
using PathSet = std::unordered_set<std::vector<T>, VectorHash<T>>;

// \brief The helper function for `all_paths`
//
// We extract each path by recursively exploring the tree using a DFS, and
// keeping track of the call stack as we traverse. For each path, we
//
// \param node The node to recurse on
// \param ancestors The chain of ancestors for `node
// \param res The result vector containing every path from the root to each leaf
template <typename T>
void all_paths_helper(const BinaryTreeNode<T> *node, std::vector<T> &ancestors,
                      PathSet<T> &res) {
    // The empty tree: no node, we can't do anything so we can terminate the
    // chain of computation here
    if (!node) {
        return;
    }
    ancestors.push_back(node->value);

    // If the current node doesn't have any children, it's a leaf, so we push
    // back the current chain of ancestors to the result
    //
    // If it's not a leaf, then we keep recursing down the left and right
    // subtrees
    if (!node->has_children()) {
        res.insert(ancestors);
    } else {
        all_paths_helper(node->left, ancestors, res);
        all_paths_helper(node->right, ancestors, res);
    }
    // Pop off the current node as we pop off the current call stack and the
    // function traverses another subtree, or terminates the search
    ancestors.pop_back();
}

// Return every path from the root node to each leaf
//
// This method is just a shim around `all_paths_helper`, which we use to
template <typename T> auto all_paths(const BinaryTreeNode<T> *root) {
    std::vector<T> ancestors{};
    PathSet<T> res{};
    all_paths_helper(root, ancestors, res);
    return res;
}

TEST_CASE("empty tree", "[587]") {
    auto res = all_paths<int>(nullptr);
    REQUIRE(res.empty());
}

TEST_CASE("one node", "[587]") {
    auto node = BinaryTreeNode(0);
    auto res = all_paths(&node);
    PathSet<int> expected{{0}};
    REQUIRE(res == expected);
}

TEST_CASE("supplied example", "[587]") {
    using std::make_unique;
    using std::unique_ptr;

    // We use a lambda here so we can create a const vector
    const auto arena = [] {
        // We can't use an initializer list because that requires the copy
        // constructor, so we use `push_back` to use unique_ptr's move semantics
        std::vector<unique_ptr<BinaryTreeNode<int>>> v;
        v.push_back(make_unique<BinaryTreeNode<int>>(1));
        v.push_back(make_unique<BinaryTreeNode<int>>(2));
        v.push_back(make_unique<BinaryTreeNode<int>>(3));
        v.push_back(make_unique<BinaryTreeNode<int>>(4));
        v.push_back(make_unique<BinaryTreeNode<int>>(5));
        v[0]->left = v[1].get();
        v[0]->right = v[2].get();
        v[2]->left = v[3].get();
        v[2]->right = v[4].get();
        return v;
    }();
    const auto root = arena[0].get();
    PathSet<int> expected{
        {1, 2},
        {1, 3, 4},
        {1, 3, 5},
    };
    auto res = all_paths(root);
    REQUIRE(res == expected);
}
} // namespace p587
