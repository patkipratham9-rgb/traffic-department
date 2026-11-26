from traffic_fine import calculate_fine


def test_no_helmet():
    assert calculate_fine("No Helmet") == 500


def test_signal_jumping():
    assert calculate_fine("Signal Jumping") == 1000


def test_over_speeding():
    assert calculate_fine("Over Speeding") == 2000