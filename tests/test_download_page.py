from core.base_url import Urls


def test_download_file_name(download_page):
    download_page.actions.goto(Urls.DOWNLOAD)

    download = download_page.download_file(2)
    actual = download_page.get_file_name(2)

    assert actual == download.suggested_filename, (
        f"Expected: '{download.suggested_filename}', "
        f"Actual: '{actual}'"
    )