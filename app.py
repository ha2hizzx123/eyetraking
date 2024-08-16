from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용, 필요에 따라 특정 도메인으로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EyeTrackingData(BaseModel):
    secction_1: bool
    secction_2: bool
    secction_3: bool

@app.post("/eyetracking")
def receive_eye_tracking_data(data: EyeTrackingData):
    # 수신한 데이터 처리 로직 (예: 로깅, 데이터베이스 저장 등)
    return {"message": "Data received", "data": data}
