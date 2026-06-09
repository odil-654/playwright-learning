class SearchResultsPage:
    def __init__(self, page):
        self.page = page

        self.filter_select = page.get_by_test_id("filter-sort")
        self.article_prices = page.locator(".article-price")
        self.loader = page.get_by_test_id("results-loader-svg")

    def wait_until_loaded(self):
        self.filter_select.wait_for(state="visible")
        self.article_prices.first.wait_for(state="visible")

    def apply_filter(self, filter_type):
        self.filter_select.select_option(label=str(filter_type))
        self.loader.wait_for(state="visible")
        self.loader.wait_for(state="hidden")

    def get_first_prices(self, n):
        prices = []

        for index in range(n):
            price = self.article_prices.nth(index).get_attribute("data-price")
            prices.append(int(price))

        return prices