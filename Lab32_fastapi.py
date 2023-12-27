from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"key": "Hello World"}

@app.post("/detect")
def detect():
    return {"key": "detect state of driving !"}


uvicorn.run(app, port=8000,host='0.0.0.0')