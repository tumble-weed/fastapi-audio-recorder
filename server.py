from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

#origins = ["http://localhost:10000"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#'''
#app.mount("/", StaticFiles(directory=".", html=True), name="static")
#@app.get("/api/data")
#def read_data():
#  return{"message": "It worked!"}
#@app.post("/uploadfile")
#async def create_upload_file(*args,**kwargs):
#@app.post("/uploadfile")
#async def create_upload_file(file: UploadFile = File(...)):
@app.get('/testing')
async def testing():
    return {'message':'hello you have reached "testing"'}

@app.post("/uploadfile")
def create_upload_file(file: UploadFile = File(..., media_type="audio/wav")):
    print("Hello")
    with open(file.filename, "wb") as audio_file:
        audio_file.write(file.file.read())
    return {"filename": file.filename}

#@app.route("/index.html")
#def index():
#    return Template('index.html')

