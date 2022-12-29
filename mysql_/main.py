import mysql_pool_name
import time

mp = mysql_pool_name.MysqlPool()

conn, cursor = mp.connect()

sql = "insert into hello value (%s)"
list1 = []
for i in range(1, 2000000):
    list1.append(i)
# 批量插入数据，
start_time = time.time()
cursor.executemany(sql, list1)
conn.commit()
print(f"插入耗时：{time.time() - start_time} 秒钟")
cursor.close()
conn.close()

# for i in range(1, 100):
#     sql = "insert into hello value (%s)"
#     try:
#         cursor.execute(sql)
#     except Exception as e:
#         print(e)
# conn.commit()
# cursor.close()
# conn.close()
