# 简体转繁体脚本

这是一个自动将代码文件中的简体中文转换为繁体中文的Python脚本。

## 功能
- 递归扫描指定目录下的文件
- 自动转换指定扩展名文件中的简体中文为繁体中文
- 保留原始文件编码(UTF-8)

## 自定义配置
在运行脚本前，您可以根据需要修改以下配置：
1. 修改`EXTENSIONS`变量设置要扫描的文件扩展名（默认：`.tsx`, `.ts`, `.js`, `.jsx`, `.json`, `.md`, `.txt`）
2. 修改`TARGET_DIR`变量设置要扫描的文件夹路径（默认：`/Users/jfoy/Desktop/projects/crm_react/src`）

## 使用方法
1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行脚本：
```bash
python convert_simplified_to_traditional.py
```