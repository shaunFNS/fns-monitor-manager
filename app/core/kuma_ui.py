from app.core import selectors


class KumaUI:
    def __init__(self, page):
        self.page = page

    def click_add_monitor(self):
        self.page.get_by_role(
            "button",
            name=selectors.ADD_MONITOR_BUTTON,
        ).click()

    def select_monitor_type(self, monitor_type: str):
        self.page.locator(
            selectors.MONITOR_TYPE
        ).select_option(monitor_type)

    def set_name(self, name: str):
        self.page.locator(
            selectors.MONITOR_NAME
        ).fill(name)

    def save(self):
        self.page.locator("form:visible").get_by_role(
            "button",
            name="Save",
            exact=True,
        ).click()

        self.page.wait_for_load_state("networkidle")