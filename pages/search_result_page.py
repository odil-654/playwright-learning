class SearchResultsPage:
    def __init__(self, page):
        self.page = page

        self.filter_select = page.get_by_test_id("filter-sort")
        self.article_prices = page.locator(".article-price")

    def apply_filter(self, filter_type):
        self.filter_select.select_option(label=filter_type)
        self.page.wait_for_load_state("networkidle")

    def get_first_prices(self, n):
        prices = []

        for index in range(n):
            price = self.article_prices.nth(index).get_attribute("data-price")
            prices.append(int(price))

        return prices
