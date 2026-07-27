from app.core.kuma_client import KumaClient


def create_ping(
    group: str,
    name: str,
    hostname: str,
):
    client = KumaClient()

    try:
        client.connect()

        client.create_ping_monitor(
            group=group,
            name=name,
            hostname=hostname,
        )

    finally:
        client.disconnect()