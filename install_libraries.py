"""
 @Author: wangxi
 @Email: seal709@163.com
 @FileName: install_libraries.py.py
 @DateTime: 2023/12/12 20:45
 @SoftWare: PyCharm
"""
import os


def install_packages():
    commands = [
        'pip install PyPDF2',
        'pip install pdfminer.six',
        'pip install pdfplumber',
        'pip install pdf2image',
        'pip install Pillow',
        'brew install tesseract',
        'pip install pytesseract'
    ]

    mac_commands = [
        'brew install tesseract'
    ]

    windows_commands = [
        """
        对于Windows用户，可以参照以下步骤进行安装(https://linuxhint.com/install-tesseract-windows/)。安装软件后，需要将它们的可执行文件路径添加到计算机上的环境变量中。或者，也可以运行以下命令，使用以下代码直接将其路径包含在Python脚本中：
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        """


    ]

    for command in commands:
        os.system(command)


if __name__ == "__main__":
    install_packages()
