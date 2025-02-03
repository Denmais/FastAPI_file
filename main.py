from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"/home/dev/work/Sysel/http_file/{file.filename}"
    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}