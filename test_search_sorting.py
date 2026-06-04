from enum import StrEnum

import pytest
from playwright.sync_api import expect

from config_reader import ConfigReader
from pages.main_page import MainPage

config = ConfigReader.get_instance()


class SortFilter(StrEnum):
    LOW_TO_HIGH = "Price: low to high"
    HIGH_TO_LOW = "Price: high to low"


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize("n", [10, 15])
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

    expect(search_results_page.filter_select).to_be_visible()

    search_results_page.apply_filter(filter_type)

    prices = search_results_page.get_first_prices(n)

    if filter_type == SortFilter.LOW_TO_HIGH:
        expected_prices = sorted(prices)
    else:
        expected_prices = sorted(prices, reverse=True)

    assert prices == expected_prices, (
        f"Expected prices: {expected_prices}, "
        f"Actual prices: {prices}"
    )