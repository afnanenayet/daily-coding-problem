/*
Given a string with repeated characters, rearrange the string so that no two
adjacent characters are the same. If this is not possible, return None
*/

#include "pch.hpp"
#include <optional>

namespace p584 {

// A struct representing the entries used in the priority queue
struct pq_key {
    // The letter that this entry corresponds to
    char letter;

    // The frequency of the letter in the string
    //
    // This field is used as the priority for the priority queue
    unsigned int freq;
};

// An overload of the `<` operator that compares keys so we can use this struct
// with the priority queue class
bool operator<(const pq_key &a, const pq_key &b) { return a.freq < b.freq; }

// Given some input string, rearrange the string so no two adjacent characters
// are the same.
//
// We do this by recording the frequencies of each character, and creating a new
// string in a greedy fashion, where the next character is the one with the
// highest frequency in the remainder of the string that isn't the character we
// just visited. We then use a priority queue to insert characters in the order
// of most frequent to least frequent, updating frequencies as we use up
// characters. We also make sure not to repeat characters twice in a row by
// temporarily removing the top element so we can get the next top element.
//
// This approach is O(n) space and O(nlogn) time.
auto rearrange_chars(const std::string &input) {
    // A count of the frequency for each character in the string
    std::unordered_map<char, unsigned int> freqs;

    // The resulting string
    std::string res;

    // The priority queue that we pull from when inserting characters into the
    // new string
    std::priority_queue<pq_key> q;

    // Calculate the frequency of each character
    for (const auto &c : input) {
        freqs[c] += 1;
    }

    // Initialize the priority queue
    for (const auto &it : freqs) {
        q.push(pq_key{it.first, it.second});
    };

    // We keep track of the last entry so we don't accidentally repeat the same
    // character twice in a row, when we consume the top element, remove it, and
    // store it in this variable, and then restore the entry on the next
    // iteration.
    std::optional<pq_key> last_entry = std::nullopt;

    // Keep adding elements to the result until we exhaust the queue
    while (!q.empty()) {
        // Get the current top entry and remove it from the priority queue
        // because we can't use that letter in the next iteration, so we
        // temporarily remove it from the queue.
        auto current_top = q.top();
        q.pop();
        res += current_top.letter;

        // We restore the entry that was stored from the previous interation (if
        // there was one), since we already have the top entry without this
        // entry removed from the queue
        if (last_entry) {
            q.push(*last_entry);
            last_entry = std::nullopt;
        }

        // Decrement the frequency of the current top entry since that character
        // has already been used
        current_top.freq -= 1;

        // If we have exhausted this letter, then don't store it, so it doesn't
        // get added back to the queue in the next iteration
        if (current_top.freq > 0) {
            last_entry = std::make_optional(current_top);
        }
    }

    // If the last entry isn't null, that means that the queue was emptied but
    // all of the letters haven't been exhausted, which means that we would have
    // repeated adjacent characters
    if (last_entry.has_value()) {
        return std::optional<std::string>{};
    }
    return std::make_optional(std::move(res));
}

// Check whether a string meets the adjacency condition defined by the problem
bool adjacency_condition(const std::string &input) {
    if (input.empty()) {
        return true;
    }

    // At each iteration, check if the char at index `i` is equal to the char to
    // it's right (`i + 1`). If it is, we can bail and say the condition has not
    // been met.
    for (int i = 0; i < input.size() - 1; i++) {
        if (input[i] == input[i + 1]) {
            return false;
        }
    }
    return true;
}

TEST_CASE("adjacency condition", "[584]") {
    REQUIRE(!adjacency_condition("aaabbc"));
    REQUIRE(adjacency_condition(""));
    REQUIRE(adjacency_condition("abcdefg"));
    REQUIRE(adjacency_condition("abab"));
    REQUIRE(!adjacency_condition("aa"));
}

TEST_CASE("rearrangement possible", "[584]") {
    auto res = rearrange_chars("aaabbc");
    REQUIRE(res.has_value());
    REQUIRE(adjacency_condition(*res));
}

TEST_CASE("rearrangement not possible", "[584]") {
    REQUIRE(!rearrange_chars("aaab").has_value());
}
}; // namespace p584
