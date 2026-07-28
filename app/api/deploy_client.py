from fastapi import APIRouter

from app.models.deploy_client import DeployClient
from app.services.deploy_client import deploy_client

router = APIRouter()


@router.post("/deploy-client")
def deploy(deployment: DeployClient):
    result = deploy_client(deployment)

    return {
        "status": "success",
        "deployment": result,
    }