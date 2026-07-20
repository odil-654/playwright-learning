import random

from core.base_url import Urls


def test_slider_with_key(slider_page):
    slider_page.actions.goto(Urls.SLIDER)
    slider_page.click_to_slider()

    min_val = slider_page.get_min()
    max_val = slider_page.get_max()
    step = slider_page.get_step()

    possible_values = []
    current = min_val

    while current <= max_val:
        possible_values.append(round(current, 1))
        current += step

    possible_values = possible_values[1:-1]

    target = random.choice(possible_values)

    slider_page.move_slider_to(target)

    actual = slider_page.get_slider_value()

    assert actual == target, (
        f"Expected: '{target}', "
        f"Actual: '{actual}'"
    )