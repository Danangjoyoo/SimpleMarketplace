"""
Exception Handler Utils
"""
from chain_logging.flask import logger
from flask_toolkits import status
from flask_toolkits.responses import JSONResponse
from typing import Any, Dict

from app.database import session


class InvalidProcess(Exception):
    """
    Invalid Process
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


def handle_commit(error_message):
    try:
        session.commit()
    except Exception as error:
        message = f"{error_message or 'failed to commit'}. {error}"
        logger.error(message)
        InvalidProcess(f"{message}, {error}")