from core.base_url import Urls


def test_text_in_frames(frames_page):
    frames_page.actions.goto(Urls.FRAMES)
    assert frames_page.get_left_frame_text() == "LEFT"
    assert frames_page.get_right_frame_text() == "RIGHT"
    assert frames_page.get_bottom_text() == "BOTTOM"
    assert frames_page.get_middle_frame_text() == "MIDDLE"