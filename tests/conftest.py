import pytest
from pages.basic_auth_page import BasicAuthPage
from pages.javascript_alerts_page import JavascriptAlertsPage


@pytest.fixture
def basic_auth_page(page):
    return BasicAuthPage(page)

@pytest.fixture
def javascript_alerts_page(page):
    return JavascriptAlertsPage(page)