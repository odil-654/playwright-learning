from core.base_url import Urls


def test_windows_and_button(windows_page):
    windows_page.actions.goto(Urls.WINDOWS)
    text_1 = "New Window"
    new_page_1 = windows_page.click_and_get_new_page()
    new_page_1_text = new_page_1.locator("h3").inner_text()         #помню, что нельзя локаторы писать в тесте, я потом исправлю, хотел общий список быстрее закончить
    assert text_1 == new_page_1_text, (
        f"Expected: '{text_1}', Actual: '{new_page_1_text}'"
    )
    windows_page.actions.bring_to_front()
    text_2 = "New Window"
    new_page_2 = windows_page.click_and_get_new_page()
    new_page_2_text = new_page_2.locator("h3").inner_text()     #помню, что нельзя локаторы писать в тесте, я потом исправлю, хотел общий список быстрее закончить
    assert text_2 == new_page_2_text, (
        f"Expected: '{text_2}', Actual: '{new_page_2_text}'"
    )
    actual = windows_page.actions.bring_to_front()
    new_page_1.close()                      #тут короче непонятно, я вроде создал специально новый метод, но один фиг не использовал его, так как отдельный класс делать было лень((((
    new_page_2.close()                      #то же самое
    number_of_pages = 1
    assert number_of_pages == len(actual), (
        f"Expected: '{number_of_pages}', Actual: '{len(actual)}'"
    )