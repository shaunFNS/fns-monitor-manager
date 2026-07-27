from fastapi import APIRouter

from app.core.auth import login

router = APIRouter()


@router.post("/login-test")
def login_test():

    browser, page = login()

    title = page.title()

    browser.stop()

    return {
        "success": True,
        "title": title
    }
