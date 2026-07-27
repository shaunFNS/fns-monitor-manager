from app.core.kuma_client import KumaClient


def create_group(name: str):

    client = KumaClient()

    try:
        client.connect()
        client.create_group(name)

    finally:
        client.disconnect()