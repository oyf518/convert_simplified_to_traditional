import os
import re
from opencc import OpenCC

# 初始化OpenCC轉換器
cc = OpenCC('s2t')  # 簡體轉繁體

# 要掃描的文件擴展名
EXTENSIONS = {'.tsx', '.ts', '.js', '.jsx', '.json', '.md', '.txt'}
# 目標目錄
TARGET_DIR = '/Users/jfoy/Desktop/projects/crm_react'

# 排除的目錄
EXCLUDED_DIRS = {'node_modules', '.git'}

# 簡體中文正則表達式
ZH_CN_PATTERN = re.compile(r'[\u4e00-\u9fa5]+')

def convert_file(file_path):
    """轉換單個文件中的簡體中文為繁體中文"""
    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            # 查找並轉換所有簡體中文
            new_content = ZH_CN_PATTERN.sub(
                lambda x: cc.convert(x.group()), 
                content
            )
            
            if new_content != content:
                f.seek(0)
                f.write(new_content)
                f.truncate()
                print(f'已轉換: {file_path}')
    except Exception as e:
        print(f'處理 {file_path} 時出錯: {e}')

def scan_and_convert(directory):
    """遞歸掃描目錄並轉換文件"""
    for root, _, files in os.walk(directory):
        # 檢查是否在排除的目錄中
        if any(excluded_dir in root for excluded_dir in EXCLUDED_DIRS):
            continue
        
        for file in files:
            if os.path.splitext(file)[1] in EXTENSIONS:
                file_path = os.path.join(root, file)
                convert_file(file_path)

if __name__ == '__main__':
    print(f'開始掃描目錄: {TARGET_DIR}')
    scan_and_convert(TARGET_DIR)
    print('轉換完成')