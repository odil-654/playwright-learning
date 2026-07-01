def check_all_hovers(hovers_page):
    hovers_page.goto("https://the-internet.herokuapp.com/hovers")
    list_1 = hovers_page.get_all_items()
    