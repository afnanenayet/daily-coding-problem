import pytest

from solution_1756 import HitCounter


def test_hit_counter() -> None:
    hc = HitCounter()
    assert len(hc) == 0
    hc.record(1000)
    hc.record(1)
    assert len(hc) == 2
    assert hc.range(0, 0) == 0
    assert hc.range(0, 1) == 1
    assert hc.range(1, 1) == 1
    assert hc.range(0, 2) == 1
    assert hc.recorded_timestamps == sorted(hc.recorded_timestamps)

    hc.record(5)
    assert len(hc) == 3
    assert hc.range(1, 5) == 2
    assert hc.range(0, 3) == 1
    assert hc.range(3, 7) == 1
    assert hc.range(4, 100) == 1
    assert hc.range(0, 100) == 2
    assert hc.recorded_timestamps == sorted(hc.recorded_timestamps)

    hc.record(10)
    assert len(hc) == 4
    assert hc.range(0, 100) == 3
    assert hc.range(0, 1) == 1
    assert hc.range(0, 5) == 2
    assert hc.range(0, 10) == 3
    assert hc.range(5, 5) == 1
    assert hc.range(5, 10) == 2
    assert hc.recorded_timestamps == sorted(hc.recorded_timestamps)


def test_record_negative() -> None:
    """Making sure we raise the error."""
    hc = HitCounter()
    with pytest.raises(ValueError):
        hc.record(-1)

    with pytest.raises(ValueError):
        hc.record(-100)
