from core.base_url import Urls


def test_text_in_frames(frames_page):
    frames_page.actions.goto(Urls.FRAMES)
    actual = frames_page.get_left_frame_text()
    assert actual == "LEFT", f"Expected: 'LEFT', Actual: '{actual}'"
    actual = frames_page.get_right_frame_text()
    assert actual == "RIGHT", f"Expected: 'LEFT', Actual: '{actual}'"
    actual = frames_page.get_bottom_text()
    assert actual == "BOTTOM", f"Expected: 'BOTTOM', Actual: '{actual}'"
    actual = frames_page.get_middle_frame_text()
    assert actual == "MIDDLE", f"Expected: 'MIDDLE', Actual: '{actual}'"