from app.core.kuma_client import KumaClient


def deploy_client(deployment):
    client = KumaClient()

    result = {
        "client": deployment.client,
        "group": None,
        "created": [],
        "skipped": [],
    }

    try:
        client.connect()

        group_created = client.create_group(
            deployment.client,
        )

        if group_created:
            result["group"] = "created"
        else:
            result["group"] = "reused"

        website_monitor_name = (
            f"{deployment.client} - Website"
        )

        website_created = client.create_http_monitor(
            deployment.client,
            website_monitor_name,
            deployment.website,
        )

        if website_created:
            result["created"].append(
                website_monitor_name,
            )
        else:
            result["skipped"].append(
                website_monitor_name,
            )

        for ping in deployment.ping_targets:
            ping_monitor_name = (
                f"{deployment.client} - {ping.name}"
            )

            ping_created = client.create_ping_monitor(
                deployment.client,
                ping_monitor_name,
                ping.hostname,
            )

            if ping_created:
                result["created"].append(
                    ping_monitor_name,
                )
            else:
                result["skipped"].append(
                    ping_monitor_name,
                )

        return result

    finally:
        client.disconnect()