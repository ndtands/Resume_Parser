from transformers import LayoutLMv2ForTokenClassification, LayoutLMv2Processor
import torch
from config import *
from PIL import Image, ImageDraw,ImageFont
import numpy as np
from utils import *


class Resume_parser:
    def __init__(self, num_class: int=len(TAG2IDX)) -> None:
        self.num_class = num_class
        self.model = LayoutLMv2ForTokenClassification.from_pretrained(PRETRAIN_MODEL,num_labels=num_class)
        self.process = LayoutLMv2Processor.from_pretrained(PRETRAIN_PROCESSOR,TOKENIZERS_PARALLELISM = True)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def load_model(self, path_model: str=MODEL_PATH) -> None:
        self.model.load_state_dict(torch.load(path_model))
        print('✅ Load done')
        
    def infer(self, image) -> Image.Image:
        # Load image
        image = image.convert("RGB")

        # preprocess
        encoding = self.process(image, return_offsets_mapping=True, return_tensors="pt")
        offset_mapping = encoding.pop('offset_mapping')
        for k,v in encoding.items():
            encoding[k] = v.to(self.device)
        self.model.to(self.device)

        # inference
        outputs = self.model(**encoding)

        # posprocess
        predictions = outputs.logits.argmax(-1).squeeze().tolist()
        token_boxes = encoding.bbox.squeeze().tolist()
        width, height = image.size
        is_subword = np.array(offset_mapping.squeeze().tolist())[:,0] != 0

        true_predictions = [IDX2TAG[pred] for idx, pred in enumerate(predictions) if not is_subword[idx]]
        true_boxes = [unnormalize_box(box, width, height) for idx, box in enumerate(token_boxes) if not is_subword[idx]]
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        for prediction, box in zip(true_predictions, true_boxes):
            draw.rectangle(box, outline=TAG2COLOR[prediction])
            draw.text((box[0]+10, box[1]-10), text=prediction, fill=TAG2COLOR[prediction], font=font)
        return image