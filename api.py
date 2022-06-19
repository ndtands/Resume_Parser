from fastapi import FastAPI
from model import Resume_parser
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from io import BytesIO

# Create Input
class Input(BaseModel):
    path:str

# Load model
model = Resume_parser()
model.load_model()

api = FastAPI(title="MLOps", version='0.1.0')
@api.post('/api/predict')
def predict(input: Input):
    path = input.path
    result =  model.infer(path_image=path)
    infer_image = BytesIO()
    result.save(infer_image, "JPEG")
    infer_image.seek(0)
    return StreamingResponse(infer_image, media_type="image/jpeg")