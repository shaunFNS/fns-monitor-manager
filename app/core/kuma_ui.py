from app.core import selectors


class KumaUI:
    def __init__(self, page):
        self.page = page

    def click_add_monitor(self):
        self.page.get_by_role(
            "link",
            name="Add New Monitor",
            exact=True,
        ).click()

    def select_monitor_type(self, monitor_type: str):
        self.page.locator(
            selectors.MONITOR_TYPE,
        ).select_option(monitor_type)

    def set_name(self, name: str):
        self.page.locator(
            selectors.MONITOR_NAME,
        ).fill(name)

    def set_hostname(self, hostname: str):
        self.page.locator(
            selectors.HOSTNAME,
        ).fill(hostname)

    def set_url(self, url: str):
        self.page.locator(
            selectors.URL,
        ).fill(url)

    def set_parent_group(self, group_name: str):
        if not group_name:
            return

        if group_name.strip().lower() == "none":
            return

        self.page.locator(
            selectors.MONITOR_GROUP,
        ).select_option(label=group_name)

    def item_exists(self, name: str) -> bool:
        return (
            self.page.get_by_text(
                name,
                exact=True,
            ).count()
            > 0
        )

    def save(self):
        self.page.locator(
            "form:visible",
        ).get_by_role(
            "button",
            name="Save",
            exact=True,
        ).click()

        self.page.get_by_role(
            "link",
            name="Add New Monitor",
            exact=True,
        ).wait_for(
            state="visible",
            timeout=30000,
        )