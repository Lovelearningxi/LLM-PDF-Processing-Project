"""
 @Author: wangxi
 @Email: seal709@163.com
 @FileName: image_processor.py
 @DateTime: 2023/12/13 14:04
 @SoftWare: PyCharm
"""
# image_processor.py
# image_processor.py
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from tqdm import tqdm

def process_images_in_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    image_texts = []
    for image in tqdm(images, desc="Processing Images"):
        text = pytesseract.image_to_string(image)
        image_texts.append(text)
    return image_texts
