from app.core.kuma_client import KumaClient


def deploy_client(deployment):
    client = KumaClient()

    try:
        client.connect()

        client.create_group(
            deployment.client,
        )

        client.create_http_monitor(
            deployment.client,
            "Website",
            deployment.website,
        )

        for ping in deployment.ping_targets:
            client.create_ping_monitor(
                deployment.client,
                ping.name,
                ping.hostname,
            )

    finally:
        client.disconnect()