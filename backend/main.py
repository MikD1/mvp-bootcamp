from fastapi import FastAPI
import uvicorn

app = FastAPI(root_path="/proxy/8000")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)