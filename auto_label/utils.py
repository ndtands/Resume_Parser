import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import json


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    
    def norm(self, x:float, y:float, w:float, h:float) -> tuple:
        x_norm = x*100/self.width
        y_norm = y*100/self.height
        w_norm = w*100/self.width
        h_norm = h*100/self.height
        return (x_norm, y_norm, w_norm, h_norm)

    def de_norm(self, x_norm: float, y_norm: float, w_norm: float, h_norm: float) -> tuple:
        x = x_norm*self.width/100
        y = y_norm*self.height/100
        w = w_norm*self.width/100
        h = h_norm*self.height/100
        return (x, y, x+w, y+h)


def fill_result(width, height, x, y, w, h,text, id = None):
    return [
        {"original_width":width,
          "original_height":height,
          "image_rotation":0,
          "value":{
            "x":x,
            "y":y,
            "width":w,
            "height":h,
            "rotation":0
          },
          "id":id,
          "from_name":"bbox",
          "to_name":"image",
          "type":"rectangle",
          "origin":"manual"
        },
        {"original_width":width,
          "original_height":height,
          "image_rotation":0,
          "value":{
            "x":x,
            "y":y,
            "width":w,
            "height":h,
            "rotation":0,
            "text":[
                text
            ]
          },
          "id":id,
          "from_name":"transcription",
          "to_name":"image",
          "type":"textarea",
          "origin":"manual"
        }
    ]


def extract_pdf(path: str)-> tuple:
    image = Image.open(path)
    image = image.convert("RGB")
    width, height = image.size
    reg = Rectangle(width, height)
    ocr_df = pytesseract.image_to_data(image, output_type='data.frame')
    ocr_df = ocr_df.dropna().reset_index(drop=True)
    float_cols = ocr_df.select_dtypes('float').columns
    ocr_df[float_cols] = ocr_df[float_cols].round(0).astype(int)
    ocr_df = ocr_df.replace(r'^\s*$', np.nan, regex=True)
    coordinates = ocr_df[['left', 'top', 'width', 'height','text']]
    actual_boxes = []
    for _, row in coordinates.iterrows():
        x, y, w, h = tuple(row[:4])
        x, y, w, h = reg.norm(x, y, w, h)
        t = row[4]
        actual_boxes.append([x, y, w, h, str(t)])
    return (actual_boxes, (width, height))

def read_json(path: str) -> dict:
    object = open(path)
    data = json.load(object)
    return data

def write_json(data, path: str) -> None:
    with open(path, 'w') as f:
        json.dump(data, f)