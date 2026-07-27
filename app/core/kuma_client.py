from app.core import selectors
from app.core.auth import login
from app.core.kuma_ui import KumaUI

class KumaClient:
    def __init__(self):
        self.browser = None
        self.page = None

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

        self.page.wait_for_load_state("networkidle")

    def create_ping_monitor(
        self,
        group: str,
        name: str,
        hostname: str,
    ):
        print(
            f"Creating ping monitor: "
            f"group={group}, "
            f"name={name}, "
            f"hostname={hostname}"
        )