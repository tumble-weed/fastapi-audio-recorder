import time
from fastapi import FastAPI, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
timestr = time.strftime("%Y%m%d-%H%M%S")

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


@app.post("/file/upload")
def upload_file(file: UploadFile):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(400, detail="Invalid audio file type")
    else:
        # Handle audio file data
        # Here you can save the audio file, process it, etc.
        file_data = file.file.read()
        # Example: save the audio file
        new_filename = "{}_{}.wav".format(os.path.splitext(file.filename)[0], timestr)
        save_file_path = os.path.join(UPLOAD_DIR, new_filename)
        with open(save_file_path, "wb") as f:
            f.write(file_data)
    return {"filename": new_filename}


@app.post("/file/uploadndownload")
def upload_n_downloadfile(file: UploadFile):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(400, detail="Invalid audio file type")
    else:
        file_data = file.file.read()
        new_filename = "{}_{}.wav".format(os.path.splitext(file.filename)[0], timestr)
        # Save the audio file
        save_file_path = os.path.join(UPLOAD_DIR, new_filename)
        with open(save_file_path, "wb") as f:
            f.write(file_data)

        # Return the saved audio file as a download
        return FileResponse(
            path=save_file_path,
            media_type="audio/wav",
            filename=new_filename,
        )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
