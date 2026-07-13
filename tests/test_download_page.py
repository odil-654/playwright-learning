from core.base_url import Urls


def test_download_file_name(download_page):
    download_page.actions.goto(Urls.DOWNLOAD)
    list_1 = download_page.get_all_id()
    with download_page.page.expect_download() as download_info:
        list_1[2].click()
    download = download_info.value
    assert list_1[2].get_inner_text() == download.suggested_filename, (
        f"Expected: '{list_1[2].get_inner_text()}', "
        f"Actual: '{download.suggested_filename}'"
    )