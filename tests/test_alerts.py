from faker import Faker
from core.base_url import Urls


def test_click_for_alerts(javascript_alerts_page):
    javascript_alerts_page.actions.goto(Urls.JS_ALERT)
    javascript_alerts_page.click_js_alert()
    text_1 = javascript_alerts_page.get_result_text()
    assert text_1 == "You successfully clicked an alert", (
        f"Expected: 'You successfully clicked an alert', "
    f"Actual: '{text_1}'"
    )

def test_click_for_confirm(javascript_alerts_page):
    javascript_alerts_page.actions.goto(Urls.JS_ALERT)
    javascript_alerts_page.click_js_confirm()
    text_1 = javascript_alerts_page.get_result_text()
    assert text_1 == "You clicked: Ok", (
        f"Expected: 'You clicked: Ok',"
        f"Actual: '{text_1}'"
    )

def test_click_for_cancel(javascript_alerts_page):
    javascript_alerts_page.actions.goto(Urls.JS_ALERT)
    javascript_alerts_page.click_js_cancel()
    text_1 = javascript_alerts_page.get_result_text()
    assert text_1 == "You clicked: Cancel", (
        f"Expected: 'You clicked: Cancel', "
        f"Actual: '{text_1}'"
    )

def test_click_for_prompt(javascript_alerts_page):
    javascript_alerts_page.actions.goto(Urls.JS_ALERT)
    faker = Faker()
    random_text = faker.word()
    javascript_alerts_page.click_js_prompt(random_text)
    assert random_text in javascript_alerts_page.get_result_text(), (
        f"Expected: '{random_text}', "
        f"Actual: '{javascript_alerts_page.get_result_text()}'"
    )