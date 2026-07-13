DOMAIN = "the-internet.herokuapp.com"
BASE_URL = f"https://{DOMAIN}"


class Urls:
    BASIC_AUTH = f"{BASE_URL}/basic_auth"
    JS_ALERT = f"{BASE_URL}/javascript_alerts"
    CONTEXT_CLICK = f"{BASE_URL}/context_menu"
    SLIDER = f"{BASE_URL}/horizontal_slider"
    HOVERS = f"{BASE_URL}/hovers"
    WINDOWS = f"{BASE_URL}/windows"
    FRAMES = f"{BASE_URL}/nested_frames"
    DYNAMIC_CONTENT = f"{BASE_URL}/dynamic_content"
    SCROLL = f"{BASE_URL}/infinite_scroll"
    UPLOAD_IMAGE = f"{BASE_URL}/upload"
    DOWNLOAD = f"{BASE_URL}/download"

    @staticmethod
    def basic_auth_url(login: str, password: str) -> str:
        return f"https://{login}:{password}@{DOMAIN}/basic_auth"