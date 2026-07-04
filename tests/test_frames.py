def test_text_in_frames(frames_page):
    frames_page.goto("https://the-internet.herokuapp.com/nested_frames")
    assert frames_page.upper_left_text.inner_text() == "LEFT"
    assert frames_page.upper_right_text.inner_text() == "RIGHT"
    assert frames_page.bottom_text.inner_text() == "BOTTOM"
    assert frames_page.upper_middle_text.inner_text() == "MIDDLE"