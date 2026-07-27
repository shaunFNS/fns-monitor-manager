from app.core.browser import BrowserManager
from app.core.config import (
    KUMA_PASSWORD,
    KUMA_URL,
    KUMA_USERNAME,
)


def login():

    browser = BrowserManager(headless=True)

    page = browser.start()

    page.goto(KUMA_URL)

    page.get_by_label("Username").fill(KUMA_USERNAME)
    page.get_by_label("Password").fill(KUMA_PASSWORD)

    page.locator("button[type='submit']").click()

    page.wait_for_selector("text=Add New Monitor")

    return browser, page
