"""
Exception Handler Utils
"""
from flask_toolkits import status
from flask_toolkits.responses import JSONResponse
from typing import Any, Dict

from app.database import session


class InvalidProcess(Exception):
    """
    Exception class to handle invalid process, usage and operation error
    and raised into a response with defined HTTP status code
    """

    def __init__(
        self,
        message: str = "",
        status_code: int = 400,
        payload: Dict[str, Any] = {}
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload or {"message": message}

    @property
    def response(self):
        return JSONResponse(self.payload, self.status_code)

    @staticmethod
    def handle_exception(exception: Exception):
        """
        Handle the incoming exception
        """
        if isinstance(exception, InvalidProcess):
            raise exception

        if len(exception.args) == 1:
            error_message = exception.args[0]
        elif len(exception.args) > 1:
            error_message = ", ".join(map(str, exception.args))
        else:
            error_message = "Unidentified Error"

        raise InvalidProcess(error_message, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def application_handler(error: "InvalidProcess"):
        """
        Handle application error for InvalidProcess Exception
        """
        return JSONResponse(error.payload, error.status_code)


def handle_commit():
    """
    handle present commit

    if there are any changes happened under transaction and it raise no error
    doesn't mean it will succeed while commiting to the database.

    Some of the cases like we have some changes then we commit, next it comes to partially succeed which means partially error also.
    Commit without rollback gonna lead an issue which the partial data that already stored will gonna be hard to be completed
    if the data we committed is dependant to each other. Then we need to rollback if theres any errors.
    """
    try:
        session.commit()
    except Exception as error:
        session.rollback()
        message = f"Session commit failed. {error}"
        InvalidProcess(f"{message}, {error}")