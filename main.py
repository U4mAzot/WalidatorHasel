from fastapi import FastAPI
from pydantic import BaseModel
from validator import check_password_strength

app = FastAPI(
    title="Password Strength Validator API",
    description="API do sprawdzania siły haseł z detekcją wycieków i analizą reguł.",
    version="1.0.0"
)

class PasswordRequest(BaseModel):
    password: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/validate-password")
def validate_password(payload: PasswordRequest):
    result = check_password_strength(payload.password)
    return result