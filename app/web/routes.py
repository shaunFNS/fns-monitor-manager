from typing import Annotated

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models.deploy_client import DeployClient, PingTarget
from app.services.deploy_client import deploy_client


router = APIRouter()

templates = Jinja2Templates(
    directory="/opt/fns-monitor-manager/app/templates"
)


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "page_title": "Dashboard",
        },
    )


@router.get("/deploy", response_class=HTMLResponse)
def deploy_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="deploy.html",
        context={
            "page_title": "Deploy Client",
            "result": None,
            "error": None,
        },
    )


@router.post("/deploy", response_class=HTMLResponse)
def deploy_from_form(
    request: Request,
    client: Annotated[str, Form()],
    website: Annotated[str, Form()],
    ping_names: Annotated[str, Form()] = "",
    ping_hostnames: Annotated[str, Form()] = "",
):
    try:
        ping_name_list = [
            value.strip()
            for value in ping_names.splitlines()
            if value.strip()
        ]

        ping_hostname_list = [
            value.strip()
            for value in ping_hostnames.splitlines()
            if value.strip()
        ]

        if len(ping_name_list) != len(ping_hostname_list):
            raise ValueError(
                "Each ping monitor name must have a matching hostname."
            )

        ping_targets = []

        for name, hostname in zip(
            ping_name_list,
            ping_hostname_list,
        ):
            ping_targets.append(
                PingTarget(
                    name=name,
                    hostname=hostname,
                )
            )

        deployment = DeployClient(
            client=client.strip(),
            website=website.strip(),
            ping_targets=ping_targets,
        )

        result = deploy_client(deployment)

        return templates.TemplateResponse(
            request=request,
            name="deploy.html",
            context={
                "page_title": "Deploy Client",
                "result": result,
                "error": None,
                "form_data": {
                    "client": client,
                    "website": website,
                    "ping_names": ping_names,
                    "ping_hostnames": ping_hostnames,
                },
            },
        )

    except Exception as exc:
        return templates.TemplateResponse(
            request=request,
            name="deploy.html",
            context={
                "page_title": "Deploy Client",
                "result": None,
                "error": str(exc),
                "form_data": {
                    "client": client,
                    "website": website,
                    "ping_names": ping_names,
                    "ping_hostnames": ping_hostnames,
                },
            },
            status_code=400,
        )