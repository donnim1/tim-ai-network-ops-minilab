from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TIM Network AI Ops MiniLab running"}

@app.get("/health")
def health():
    return {"status": "ok"}