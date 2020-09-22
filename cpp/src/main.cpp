#define CATCH_CONFIG_RUNNER

#include <catch2/catch.hpp>

int main(int argc, char *argv[]) {
    // We don't care about C STDIO compability, so turning this off will speed
    // up I/O significantly
    std::ios_base::sync_with_stdio(false);
    return Catch::Session().run(argc, argv);
}

TEST_CASE("Sanity check", "[main]") { REQUIRE(true); }
