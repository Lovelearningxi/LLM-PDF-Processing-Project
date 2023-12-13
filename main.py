# main.py
from PyPDF2 import PdfReader
from tqdm import tqdm
import text_extractor
import image_processor
import table_extractor
import sys

def main(pdf_path):
    stages = 3  # 假设有三个阶段
    # 使用PyPDF2获取PDF的页数
    pdf_reader = PdfReader(pdf_path)
    page_count = len(pdf_reader.pages)

    with tqdm(total=stages, desc="Overall Progress") as pbar:
        text_content = text_extractor.extract_text_from_pdf(pdf_path, page_count)
        pbar.update(1)

        image_texts = image_processor.process_images_in_pdf(pdf_path)
        pbar.update(1)

        # 直接获得已经格式化为Markdown的表格文本
        markdown_tables = table_extractor.extract_tables_from_pdf(pdf_path)
        pbar.update(1)

        # 将所有内容合并为一个字符串
        final_content = text_content + "\n".join(image_texts) + "\n\n" + markdown_tables

        # 输出到控制台
        print(final_content)

        # 写入到Markdown文件
        with open('output_files/output.md', 'w', encoding="utf-8") as file:
            file.write(final_content)


if __name__ == "__main__":
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else 'sample.pdf'
    main(pdf_path)
