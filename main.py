# app/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from .model import weapon_detector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from starlette.background import BackgroundTask
import json
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/template")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/detect/")
async def detect_weapon(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        detections, output_image = weapon_detector.predict(image_data)

        if output_image is None:
            return JSONResponse(content={"error": "Prediction failed"}, status_code=500)

        def cleanup():
            output_image.close()
        detection_json = json.dumps(detections)

        return StreamingResponse(
            output_image,
            media_type="image/jpeg",
            headers={
                "Content-Disposition": "inline; filename=detected_image.jpg",
                "X-Detection-Data": detection_json  # Custom header for detection data
            },
            background=BackgroundTask(cleanup)
        )
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

