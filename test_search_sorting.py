import pytest

from config_reader import ConfigReader
from pages.main_page import MainPage

config = ConfigReader.get_instance()


@pytest.mark.parametrize(
    "name, n, filter_type",
    [
        ("city", 10, "Price: low to high"),
        ("city", 15, "Price: high to low"),
        ("habits", 10, "Price: low to high"),
        ("habits", 15, "Price: high to low"),
    ],
)
def test_article_prices_sorting(page, name, n, filter_type):
    page.goto(config.get("base_url"))

    main_page = MainPage(page)

    search_results_page = main_page.search_article(name)

    search_results_page.apply_filter(filter_type)

    prices = search_results_page.get_first_prices(n)

    if filter_type == "Price: low to high":
        expected_prices = sorted(prices)
    else:
        expected_prices = sorted(prices, reverse=True)

    assert prices == expected_prices, (
        f"Expected prices: {expected_prices}, "
        f"Actual prices: {prices}"
    )
