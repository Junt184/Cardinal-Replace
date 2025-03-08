# coding=utf-8
import mysql.connector
from mysql.connector import Error


def database_operations():
    try:
        # 建立管理员连接（无需指定数据库）
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='toor'
        )

        cursor = connection.cursor()

        # 配置参数
        db_name = "cardinal"

        # 删除数据库（如果存在）
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        print(f"数据库 {db_name} 已删除")

        # 创建新数据库
        cursor.execute(f"CREATE DATABASE {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"数据库 {db_name} 已创建")

    except Error as e:
        print(f"数据库操作失败: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    database_operations()