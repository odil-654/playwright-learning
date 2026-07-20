from core.base_url import Urls


def test_upload_file_page(upload_page):
    upload_page.actions.goto(Urls.UPLOAD_IMAGE)
    upload_page.upload_file("./tests/test-file.txt")
    actual = upload_page.get_success_text()
    assert actual == "File Uploaded!", (
        f"Expected: 'File uploaded!', Actual: '{actual}'"
    )

    #этот тест фейлится, хз почему, я перепроверил, в локаторе текст правильный и в задании,
    #но почему-то он всё ещё падает