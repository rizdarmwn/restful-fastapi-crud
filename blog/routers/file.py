from fastapi import APIRouter, File, UploadFile
from typing import List
import shutil

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.post("/upload")
async def upload_file(file: UploadFile = File(default=None)):
    with open(f"{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename" : file.filename,
    "content_type": file.content_type,}

@router.post("/upload_multiple")
async def upload_multiple_file(files: List[UploadFile] = File(default=None)):
    return {"filenames" : [file.filename for file in files]}
    
