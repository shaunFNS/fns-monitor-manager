from app.core.auth import login
from app.core.kuma_ui import KumaUI
from app.core import selectors


class KumaClient:
    def __init__(self):
        self.browser = None
        self.page = None
        self.ui = None

    def connect(self):
        self.browser, self.page = login()
        self.ui = KumaUI(self.page)

    def disconnect(self):
        if self.browser:
            self.browser.stop()

    def create_group(self, name: str):
        self.ui.click_add_monitor()
        self.ui.select_monitor_type("group")
        self.ui.set_name(name)
        self.ui.save()

    def create_ping_monitor(
        self,
        group: str,
        name: str,
        hostname: str,
    ):
        self.ui.click_add_monitor()
        self.ui.select_monitor_type("ping")
        self.ui.set_name(name)

        self.page.locator(
            selectors.HOSTNAME,
        ).fill(hostname)

        self.ui.set_parent_group(group)
        self.ui.save()

    def create_http_monitor(
    self,
    group: str,
    name: str,
    url: str,
    ):
        self.ui.click_add_monitor()
        self.ui.select_monitor_type("http")
        self.ui.set_name(name)
        self.ui.set_url(url)
        self.ui.set_parent_group(group)
        self.ui.save()