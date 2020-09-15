#include "pch.hpp"

/*
 You are given a list of (website, user) pairs that represent users visiting
websites. Come up with a program that identifies the top k pairs of websites
with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

```
[('a', 1), ('a', 3), ('a', 5),
('b', 2), ('b', 6),
('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
('d', 4), ('d', 5), ('d', 6), ('d', 7),
('e', 1), ('e', 3), ('e': 5), ('e', 6)]
```

Then a reasonable similarity metric would most likely conclude that a and e are
the most similar, so your program should return [('a', 'e')].

The similarity metric/heuristic is not defined, and the question implies that
the interviewee should write their own.
 */
namespace p586 {
// A record indicating that a user visited a website
struct UserWebsiteRecord {
    std::string website;
    unsigned int user;
};

// A set of user IDs
using UserSet = std::unordered_set<int>;

// A map of website names to a set of user IDs
using SiteUserMap = std::unordered_map<std::string, std::unordered_set<int>>;

// A similarity result to be used in the heap
struct SimilarityResult {
    // The similarity heuristic between the two sites
    float score;
    // The name of the first website
    std::string a;
    // The name of the second website
    std::string b;
};

// A pair of websites with a custom equality operator
//
// A pairing is considered equal if a == a and b == b, or if a == b and b == a,
// since the ordering doesn't matter
using WebsitePair = std::unordered_set<std::string>;

// Given two records, return how similar they are
//
// The similarity heuristic is the ratio of the users that intersect to the
// union of all of the users between two user sets.
float similarity_heuristic(const UserSet &a, const UserSet &b) noexcept {
    // Find the intersection of the two sets
    UserSet intersection;
    std::set_intersection(a.begin(), a.end(), b.begin(), b.end(),
                          std::inserter(intersection, intersection.begin()));
    // Find the union of the two sets
    UserSet all;
    std::set_union(a.begin(), a.end(), b.begin(), b.end(),
                   std::inserter(all, all.begin()));

    // If the union of both sets is zero, bail early to avoid a divide-by-zero
    // error
    if (all.size() == 0) {
        return 0;
    }
    // Compute the ratio of intersecting elements to the total number of
    // distinct elements
    return static_cast<float>(intersection.size()) /
           static_cast<float>(all.size());
}

// Return the `k` most-similar websites given a list of records showing which
// users visited which websites and `k`. If there are less than `k` records
// provided, this method will return the number of records provided, providing a
// best-effort result.
//
// This heuristic will rank the algorithms by the number of users a website has
// in common, subtracted by the number of users websites don't have in common.
auto k_most_similar(const std::vector<UserWebsiteRecord> &records,
                    unsigned int k) noexcept {
    // First we need to create a mapping of sites and all of the visitors for
    // that site
    SiteUserMap m;

    for (const auto &record : records) {
        m[record.website].insert(record.user);
    }

    // A vector of references to the site names, we use this so we can iterate
    // through each pair without repeating pairs. Ex: we don't want to check [b,
    // a] if we already have [a, b]
    std::vector<std::string> site_names;

    for (const auto &[name, _] : m) {
        site_names.push_back(name);
    }

    // Comparison function for the priority queue
    auto cmp = [](const SimilarityResult &a, const SimilarityResult &b) {
        return a.score < b.score;
    };

    // A priority queue to hold the highest similarity results as they come
    std::priority_queue<SimilarityResult, std::vector<SimilarityResult>,
                        decltype(cmp)>
        pq(cmp);

    // We iterate through each possible pair of websites to calculate their
    // similarity heuristic
    for (int i = 0; i < site_names.size(); i++) {
        for (int j = i + 1; j < site_names.size(); j++) {
            auto site_a = site_names[i];
            auto site_b = site_names[j];
            float score = similarity_heuristic(m[site_a], m[site_b]);
            pq.push(SimilarityResult{score, site_a, site_b});
        }
    }

    // The result vector
    std::vector<WebsitePair> res;
    res.reserve(k);

    // We take the top k most similar elements
    for (auto i = 0; i < std::min<size_t>(k, pq.size()); i++) {
        auto similarity_res = pq.top();
        pq.pop();
        res.push_back({similarity_res.a, similarity_res.b});
    }
    return res;
}

TEST_CASE("provided example", "[586]") {
    std::vector input{UserWebsiteRecord{"a", 1},
                      {"a", 3},
                      {"a", 5},
                      {"b", 2},
                      {"b", 6},
                      {"c", 1},
                      {"c", 2},
                      {"c", 3},
                      {"c", 4},
                      {"c", 5},
                      {"d", 4},
                      {"d", 5},
                      {"d", 6},
                      {"d", 7},
                      {"e", 1},
                      {"e", 3},
                      {"e", 5},
                      {"e", 6}};
    std::vector expected = {
        WebsitePair{"a", "e"},
    };
    REQUIRE(k_most_similar(input, 1) == expected);
}
}; // namespace p586
