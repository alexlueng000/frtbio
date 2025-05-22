import pandas as pd
import pymysql
from sqlalchemy import create_engine

# ==== 修改为你的MySQL连接信息 ====
host = 'localhost'
port = 3306
user = 'root'
password = '123456'
database = 'bidding_emails'
table_name = 'company_info'

# ==== 读取CSV文件 ====
csv_path = 'company_info.xlsx'  # 替换为你的文件路径
df = pd.read_excel(csv_path)  # 如果是Excel导出的CSV用GBK试试

# print(df)

if '邮箱密码' in df.columns:
    df = df.drop(columns=['邮箱密码'])

df.columns = [
    'company_type', 'company_name', 'short_name', 'contact_person',
    'last_name', 'last_name_traditional', 'phone',
    'email', 'address', 'english_address'
]

print(df)

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

with engine.connect() as conn:
    from sqlalchemy import text
    conn.execute(text(create_table_sql))

# ==== 写入数据库 ====
df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("✅ 已成功导入（不含邮箱密码）！")