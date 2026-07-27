from app.monitors.base import BaseMonitor


class PingMonitor(BaseMonitor):

    def __init__(
        self,
        client,
        group,
        name,
        hostname,
    ):
        super().__init__(client)

        self.group = group
        self.name = name
        self.hostname = hostname

    def create(self):

        print(
            f"Creating Ping Monitor: "
            f"{self.name}"
        )