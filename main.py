from fastapi import FastAPI

app = FastAPI(title="Password Validator API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
    