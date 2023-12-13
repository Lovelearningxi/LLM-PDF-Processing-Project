"""
 @Author: wangxi
 @Email: seal709@163.com
 @FileName: text_extractor.py
 @DateTime: 2023/12/13 14:04
 @SoftWare: PyCharm
"""
# text_extractor.py
# text_extractor.py
from pdfminer.high_level import extract_text
from tqdm import tqdm

def extract_text_from_pdf(pdf_path, page_count):
    text = ""
    for page_number in tqdm(range(page_count), desc="Extracting Text"):
        text += extract_text(pdf_path, page_numbers=[page_number])
    return text

