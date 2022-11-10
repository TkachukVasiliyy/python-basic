from fastapi import APIRouter

router = APIRouter(prefix="/ping",
                   tags=["ping"]
                   )


@router.get("")
def ping():
    return {
        "message": "pong"
    }


@router.post("")
def create_ping(data: dict):
    return {
        "message": data,
    }


