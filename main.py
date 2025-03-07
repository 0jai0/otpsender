from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from instagrapi import Client

app = FastAPI() 
 
class OTPRequest(BaseModel):
    username: str
    password: str
    user_id: str
    otp: str

@app.post("/send_otp/")
def send_otp(data: OTPRequest):
    cl = Client()
    try:
        cl.login(data.username, data.password)
        recipient_id = cl.user_id_from_username(data.user_id)
        cl.direct_send(f"Your OTP is: {data.otp}", [recipient_id])
        return {"success": True, "message": "OTP sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


uvicorn main:app --reload