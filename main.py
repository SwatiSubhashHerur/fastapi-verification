from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Verification API is running"}

# Email verification
@app.get("/verify-email/")
def verify_email(email: str):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return {"email": email, "valid": True}
    return {"email": email, "valid": False}

# Phone verification
@app.get("/verify-phone/")
def verify_phone(phone: str):
    if phone.isdigit() and len(phone) == 10:
        return {"phone": phone, "valid": True}
    return {"phone": phone, "valid": False}

# Password check
@app.get("/verify-password/")
def verify_password(password: str):
    if len(password) >= 8:
        return {"password": password, "strong": True}
    return {"password": password, "strong": False}