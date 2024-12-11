import web.home


def test_home():
    assert web.home.get_home(request=None) != ""
