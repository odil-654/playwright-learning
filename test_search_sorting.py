from enum import StrEnum

import pytest

from config_reader import ConfigReader
from pages.main_page import MainPage

config = ConfigReader.get_instance()


class SortFilter(StrEnum):
    LOW_TO_HIGH = "Price: low to high"
    HIGH_TO_LOW = "Price: high to low"


@pytest.mark.parametrize(
    "name, n",
    [
        ("city", 10),
        ("city", 15),
        ("habits", 10),
        ("habits", 15),
    ],
)
@pytest.mark.parametrize(
    "filter_type",
    [
        SortFilter.LOW_TO_HIGH,
        SortFilter.HIGH_TO_LOW,
    ],
)
def test_article_prices_sorting(page, name, n, filter_type):
    page.goto(config.get("base_url"))

    main_page = MainPage(page)

    search_results_page = main_page.search_article(name)

    search_results_page.wait_until_loaded()

    search_results_page.apply_filter(filter_type)

    prices = search_results_page.get_first_prices(n)

    expected_prices = sorted(
        prices,
        reverse=filter_type == SortFilter.HIGH_TO_LOW,
    )

    assert prices == expected_prices, (
        f"Expected prices: {expected_prices}, "
        f"Actual prices: {prices}"
    )