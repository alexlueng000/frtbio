import os

# 定义 short_name 列表
short_names = [
    'FW', 'LD', 'DG', 'SN', 'ZH', 'QF', 'ZY',
    'JY', 'YY', 'QH', 'BZC', 'LH', 'HCX'
]

# 要创建文件的目录（当前目录）
output_dir = "app/email_templates"

# 执行创建文件
for short_name in short_names:
    filename = f"C10_{short_name}.html"
    filepath = os.path.join(output_dir, filename)

    # 创建空文件
    with open(filepath, "w", encoding="utf-8") as f:
        pass  # 空内容

    print(f"已创建：{filename}")