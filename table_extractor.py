"""
 @Author: wangxi
 @Email: seal709@163.com
 @FileName: table_extractor.py
 @DateTime: 2023/12/13 14:05
 @SoftWare: PyCharm
"""
# table_extractor.py
import pdfplumber
# table_extractor.py
import pdfplumber


def format_table_to_markdown(table):
    # 将表格数据转换为 Markdown 格式
    header_separator = ['---'] * len(table[0])
    markdown_table = ['| ' + ' | '.join(table[0]) + ' |', '|' + '|'.join(header_separator) + '|']
    for row in table[1:]:
        # 处理换行问题，将内部的换行转换为 Markdown 的 <br>
        formatted_row = ['<br>'.join(cell.split('\n')) for cell in row]
        markdown_table.append('| ' + ' | '.join(formatted_row) + ' |')
    return '\n'.join(markdown_table)


def extract_tables_from_pdf(pdf_path):
    # 提取PDF中的表格并转换为 Markdown 格式
    all_tables_markdown = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            for table in page_tables:
                markdown_table = format_table_to_markdown(table)
                all_tables_markdown.append(markdown_table)
    return '\n\n'.join(all_tables_markdown)  # 用两个换行符分隔不同的表格


# 如果需要，这里还可以添加一个检查函数，以确认表格是否被正确提取并格式化
def check_table(table):
    # 检查表格是否有标题行
    if len(table) < 2:
        return False
    # 检查表格是否有数据行
    if len(table[1]) < 1:
        return False
    # 检查表格是否有足够的列
    if len(table[0]) < 2:
        return False
    return True

# def extract_tables_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             for table in page.extract_tables():
#                 tables.append(table)
#         return tables
