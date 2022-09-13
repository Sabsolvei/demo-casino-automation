import pytest


@pytest.mark.usefixtures("driver")
class TestsLogin:

    def test_login(self):
        assert True
