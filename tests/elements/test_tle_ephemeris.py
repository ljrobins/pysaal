from pysaal.elements import TLEEphemeris


def test_from_tle(expected_tle):
    ephem = TLEEphemeris.from_tle(expected_tle, expected_tle.epoch, expected_tle.epoch + 1, 60)

    assert ephem[0].numpy_array.shape == (27,)
    assert ephem.numpy_array.shape == (1441, 27)
    assert len(ephem) == 1441
    assert ephem[-1].position.x == -6000.682447771027
    assert ephem[-1].position.y == 2024.4265984573651
    assert ephem[-1].position.z == -2456.1508465967677
    assert ephem[-1].velocity.x == -3.5882907116585194
    assert ephem[-1].velocity.y == -4.171760080775311
    assert ephem[-1].velocity.z == 5.333708174720774
