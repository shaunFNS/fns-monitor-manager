from app.core.kuma_client import KumaClient

def create_http(monitor):
    client = KumaClient()

    try:
        client.connect()
        client.create_http_monitor(
            monitor.group,
            monitor.name,
            monitor.url,
        )
    finally:
        client.disconnect()