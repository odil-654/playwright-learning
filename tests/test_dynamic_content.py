def test_tutorial_how_to_test_dynamic_content(dynamic_content_page):
    dynamic_content_page.goto('https://the-internet.herokuapp.com/dynamic_content')
    list_1 = dynamic_content_page.get_all_src()
    while True:
        if len(set(list_1)) < len(list_1):
            break
        else:
            dynamic_content_page.reload()
            list_1 = dynamic_content_page.get_all_src()

    assert len(set(list_1)) < len(list_1)
