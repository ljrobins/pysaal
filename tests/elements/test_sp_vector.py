import pytest

from pysaal.configs import MAX_DESIGNATOR_LENGTH, MAX_SATELLITE_ID


def test_designator(expected_sp_vector):
    expected_sp_vector.designator = "12345"
    assert expected_sp_vector.designator == "12345"
    with pytest.raises(ValueError, match="Designator cannot exceed"):
        expected_sp_vector.designator = "".join(["A" for _ in range(MAX_DESIGNATOR_LENGTH + 1)])


def test_satellite_id(expected_sp_vector):
    expected_sp_vector.satellite_id = 25545
    assert expected_sp_vector.satellite_id == 25545
    with pytest.raises(ValueError, match="Satellite ID cannot exceed"):
        expected_sp_vector.satellite_id = MAX_SATELLITE_ID + 1
