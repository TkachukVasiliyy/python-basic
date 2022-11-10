from fastapi import FastAPI
from starlette import status
from fastapi.exception_handlers import http_exception_handler
from starlette.responses import JSONResponse
from homework_03.view import router as ping
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
app.include_router(ping)


@app.get("/")
def root():
    return {"Hello"}


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    if (isinstance(exception, StarletteHTTPException)
            and exception.detail != "Not Found"):
        return await http_exception_handler(request, exception)

    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str("Incorrect data"),
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )