from PIL import Image
import time
from numpy import imag
import streamlit as st
from model import Resume_parser
import fitz
from pdf2image import convert_from_path

def get_pdf_size(pdf_path):
    doc = fitz.open(pdf_path)
    pdf_size = (int(doc[0].rect.width), int(doc[0].rect.height))
    return pdf_size
def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    pdf_size = get_pdf_size(pdf_path)
    for i in range(len(images)):
        images[i] = images[i].resize(pdf_size)
    return images

@st.cache(allow_output_mutation=True)
def load_model():
    model = Resume_parser()
    model.load_model()
    return model
   
model = load_model()

def main():
    type_input = st.sidebar.selectbox(label='Type Resume', options=['image','pdf'], index=1)
    if type_input == 'image':
        uploaded_file = st.sidebar.file_uploader("", type=['jpg','png','jpeg']) 
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.sidebar.image(image)
        is_predict = st.button('Click here to predict')
        if is_predict and uploaded_file is not None:
            start = time.time()
            image = model.infer(image=image)
            total_time = time.time() - start
            st.image(image, caption = 'Resume predict')
            st.text(f'Inference time: {total_time:0.4f} s')
    elif type_input == 'pdf':
        uploaded_file = st.sidebar.file_uploader("", type=['pdf']) 
        if uploaded_file is not None:
            with open('file.pdf','wb') as f:
                f.write(uploaded_file.getvalue())
            start = time.time()
            images = convert_pdf_to_images('file.pdf')
            for image in images:
                predict = model.infer(image)
                st.image(predict, caption = 'Resume predict')
            total_time = time.time() - start
            st.text(f'Inference time: {total_time:0.4f} s')
if __name__ == '__main__':
    main()

