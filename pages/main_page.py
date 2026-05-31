from pages.search_result_page import SearchResultsPage
from playwright.sync_api import expect


class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.get_by_test_id("search-input")


    def search_article(self, name):
        self.search_input.fill(name)
        self.search_input.press("Enter")

        search_results_page = SearchResultsPage(self.page)
        expect(search_results_page.filter_select).to_be_visible()

        return search_results_page

