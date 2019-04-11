from orchestration.tmp import get_fabs


def test_get_fabs():
    assert get_fabs(0) == 0
    assert get_fabs(-1) == 1
    assert get_fabs(1.1) == 1.1
