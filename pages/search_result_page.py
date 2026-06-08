class SearchResultsPage:
    def __init__(self, page):
        self.page = page

        self.filter_select = page.get_by_test_id("filter-sort")
        self.article_prices = page.locator(".article-price")

    def wait_until_loaded(self):
        self.filter_select.wait_for(state="visible")
        self.article_prices.first.wait_for(state="visible")

    def apply_filter(self, filter_type):
        self.filter_select.select_option(label=str(filter_type))

    def wait_until_prices_sorted(self, n, reverse=False):
        self.page.wait_for_function(
            """([selector, count, reverse]) => {
                const prices = Array.from(document.querySelectorAll(selector))
                    .slice(0, count)
                    .map(element => Number(element.getAttribute("data-price")));

                if (prices.length < count) {
                    return false;
                }

                const sortedPrices = [...prices].sort((a, b) => {
                    return reverse ? b - a : a - b;
                });

                return prices.every((price, index) => price === sortedPrices[index]);
            }""",
            arg=[".article-price", n, reverse],
        )

    def get_first_prices(self, n):
        prices = []

        for index in range(n):
            price = self.article_prices.nth(index).get_attribute("data-price")
            prices.append(int(price))

        return prices