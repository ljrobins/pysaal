import pytest


def test_semi_major_axis(expected_classical, expected_keplerian):
    assert expected_classical.semi_major_axis == pytest.approx(expected_keplerian.semi_major_axis)
