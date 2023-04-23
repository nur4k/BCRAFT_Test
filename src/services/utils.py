import os
import shutil
import uuid

from fastapi import UploadFile


async def create_image(file: UploadFile) -> None:
    with open(f"media/{file.filename}", "wb") as image:
        shutil.copyfileobj(file.file, image)

async def generate_uniquie_name(filename: str) -> str:
    filename = filename.split(".")[-1]
    return f"{uuid.uuid4()}.{filename}"

async def remove_image(filename: str) -> None:
    if os.path.isfile(f"media/{filename}"):
        os.remove(f"media/{filename}")
