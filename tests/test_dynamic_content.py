def test_tutorial_how_to_test_dynamic_content(dynamic_content_page):
    dynamic_content_page.goto('https://the-internet.herokuapp.com/dynamic_content')
    list_1 = dynamic_content_page.get_all_src()
    src_1 = list_1[0]
    src_2 = list_1[1]
    src_3 = list_1[2]
    while True:
        if src_1 == src_2 or src_2 == src_3 or src_3 == src_1:
            break
        else:
            dynamic_content_page.reload()
            list_1 = dynamic_content_page.get_all_src()
            src_1 = list_1[0]
            src_2 = list_1[1]
            src_3 = list_1[2]

    assert src_1 == src_2 or src_2 == src_3 or src_3 == src_1