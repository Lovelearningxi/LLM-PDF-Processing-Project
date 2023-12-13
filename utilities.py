"""
 @Author: wangxi
 @Email: seal709@163.com
 @FileName: utilities.py
 @DateTime: 2023/12/13 14:05
 @SoftWare: PyCharm
"""
# utilities.py
import os


def clean_up_temp_files(*files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
