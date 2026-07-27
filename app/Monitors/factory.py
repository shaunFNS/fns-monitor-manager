from app.monitors.ping import PingMonitor


class MonitorFactory:

    @staticmethod
    def create(
        monitor_type,
        client,
        **kwargs,
    ):

        if monitor_type == "ping":
            return PingMonitor(client, **kwargs)

        raise ValueError(
            f"Unknown monitor type: {monitor_type}"
        )