from laxleague.guardian import Guardian


def test_construction():
    g = Guardian('Mary', 'Jonney')
    assert 'Mary' == g.firstname
    assert 'Jonney' == g.lastname