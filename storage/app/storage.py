"""
"""
import os
import time
from flask import send_file
from flask_toolkits import APIRouter, File, Path
from werkzeug.datastructures import FileStorage

from app.utils import InvalidProcess


storage_router = APIRouter("storage", __name__)


@storage_router.get("/storage/<file_path>")
def get_file(file_path: str = Path("")):
    local_path = f"/storage.d/{file_path}"
    if not os.path.isfile(local_path):
        raise InvalidProcess("file not found", 403)
    return send_file(local_path)


@storage_router.post("/add")
def save_file(file: FileStorage = File()):
    try:
        extension = file.filename.split(".")[-1]
        extension = f".{extension}" if extension else ""
        file_path = f"{time.time_ns()}{extension}"
        file.save(f"/storage.d/{file_path}")

        result = {"url": f"http://localhost:9100/{file_path}"}
        return result

    except Exception as error:
        raise InvalidProcess(f"save file failed : {error}")
