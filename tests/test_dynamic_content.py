from core.base_url import Urls


def test_tutorial_how_to_test_dynamic_content(dynamic_content_page):
    dynamic_content_page.actions.goto(Urls.DYNAMIC_CONTENT)
    list_1 = dynamic_content_page.get_all_src()
    max_attempts = 50
    attempts = 0
    while True:
        if len(set(list_1)) < len(list_1):
            break
        if attempts >= max_attempts:
            raise TimeoutError("Maximum number of attempts exceeded.")
        else:
            dynamic_content_page.actions.reload()
            list_1 = dynamic_content_page.get_all_src()
            attempts += 1
