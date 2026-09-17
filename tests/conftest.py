import pytest
from pages.basic_auth_page import BasicAuthPage
from pages.context_page import ContextPage
from pages.download_page import DownloadPage
from pages.dynamic_content_page import DynamicContentPage
from pages.hovers_page import HoversPage
from pages.javascript_alerts_page import JavascriptAlertsPage
from pages.slider_page import SliderPage
from pages.windows_page import WindowsPage
from pages.frames_page import FramesPage
from pages.scroll_page import ScrollPage
from pages.upload_page import UploadPage
from core.logger import setup_logging


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

@pytest.fixture
def frames_page(page):
    return FramesPage(page)

@pytest.fixture
def dynamic_content_page(page):
    return DynamicContentPage(page)

@pytest.fixture
def scroll_page(page):
    return ScrollPage(page)

@pytest.fixture
def upload_page(page):
    return UploadPage(page)

@pytest.fixture
def download_page(page):
    return DownloadPage(page)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()