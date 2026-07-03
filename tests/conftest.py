import pytest
from pages.basic_auth_page import BasicAuthPage
from pages.context_page import ContextPage
from pages.hovers_page import HoversPage
from pages.javascript_alerts_page import JavascriptAlertsPage
from pages.slider_page import SliderPage


@pytest.fixture
def basic_auth_page(page):
    return BasicAuthPage(page)

@pytest.fixture
def javascript_alerts_page(page):
    return JavascriptAlertsPage(page)

@pytest.fixture
def context_page(page):
    return ContextPage(page)

@pytest.fixture
def slider_page(page):
    return SliderPage(page)

@pytest.fixture
def hovers_page(page):
    return HoversPage(page)

@pytest.fixture
def windows_page(page):
    return WindowsPage(page)
