import pandas as pd
import pymysql
from sqlalchemy import create_engine

# ==== 修改为你的MySQL连接信息 ====
host = '127.0.0.1'
port = 3306
user = 'testuser'
password = 'test123'
database = 'bidding_emails'
table_name = 'company_info'

# ==== 读取CSV文件 ====
# csv_path = 'company_info.xlsx'  # 替换为你的文件路径
# df = pd.read_excel(csv_path)  # 如果是Excel导出的CSV用GBK试试

# print(df)

# if '邮箱密码' in df.columns:
#     df = df.drop(columns=['邮箱密码'])

# df.columns = [
#     'company_type', 'company_name', 'short_name', 'contact_person',
#     'last_name', 'last_name_traditional', 'phone',
#     'email', 'address', 'english_address'
# ]

# print(df)

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4')

with pymysql.connect(host=host, user=user, password=password) as conn:
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} DEFAULT CHARACTER SET utf8mb4;")
    conn.commit()

# ==== 创建表结构（不含邮箱密码） ====
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_type VARCHAR(100),
    company_name VARCHAR(255),
    short_name VARCHAR(100),
    contact_person VARCHAR(100),
    last_name VARCHAR(100),
    last_name_traditional VARCHAR(100),
    phone VARCHAR(100),
    email VARCHAR(255),
    address TEXT,
    english_address TEXT
) CHARACTER SET utf8mb4;
"""

# 创建project_info表
create_project_info_table = f"""
CREATE TABLE IF NOT EXISTS project_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255),
    contract_number VARCHAR(100),
    tender_number VARCHAR(100),
    project_type VARCHAR(100),
    p_serial_number VARCHAR(100),
    l_serial_number VARCHAR(100),
    f_serial_number VARCHAR(100),
    purchaser VARCHAR(255),
    company_b_name VARCHAR(255),
    company_c_name VARCHAR(255),
    company_d_name VARCHAR(255),
    a1 TINYINT(1),
    a2 TINYINT(1),
    b3 TINYINT(1),
    b4 TINYINT(1),
    b5 TINYINT(1),
    b6 TINYINT(1),
    c7 TINYINT(1),
    c8 TINYINT(1),
    c9 TINYINT(1),
    c10 TINYINT(1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4;
"""

with engine.connect() as conn:
    from sqlalchemy import text
    conn.execute(text(create_project_info_table))

# ==== 写入数据库 ====
# df.to_sql(table_name, con=engine, if_exists='append', index=False)

# print("✅ 已成功导入（不含邮箱密码）！")
print("创建project_info表成功！")