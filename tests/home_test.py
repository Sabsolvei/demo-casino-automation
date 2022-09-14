import pytest

from steps.home_step import HomeStep


@pytest.mark.usefixtures("driver", "class_setup")
class TestsHome:

    @pytest.fixture
    def class_setup(self):
        self.home_step = HomeStep(self.driver)

    @pytest.mark.regression
    @pytest.mark.parametrize("expected", ["theme-light", "theme-dark"])
    def test_theme(self, expected):
        self.home_step.click_gotit_button()
        self.home_step.click_theme_switcher_toggle()
        actual = self.home_step.get_theme_class()
        if expected not in actual:
            self.home_step.click_theme_switcher_toggle()
            actual = self.home_step.get_theme_class()
        assert actual == expected

