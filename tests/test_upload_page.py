def test_upload_file_page(upload_page):
    upload_page.goto("https://the-internet.herokuapp.com/upload")
    upload_page.upload_file("./tests/test-file.txt")
    assert upload_page.success_text.get_text_content() == "File Uploaded!"

    #этот тест фейлится, хз почему, я перепроверил, в локаторе текст правильный и в задании,
    #но почему-то он всё ещё падает