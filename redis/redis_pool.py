import redis
import time

redis_pool = redis.ConnectionPool(host='192.168.1.133', port=6379, password='123456', db=0)

redis_conn = redis.Redis(connection_pool=redis_pool)

# redis_conn.set("name", "陆明通", ex=1400)
# redis_conn.set("name1", "陆明通111", ex=1400)
# info = redis_conn.get("name")
# time.sleep(13)
# print(info.decode('utf-8'))
# for i in range(1, 100):
#     redis_conn.set('user%s' % i, str({'name': '李四', 'city': '厦门', 'age': 18, 'sex': '女'}))
# result = redis_conn.mget("name", "name1")
print(redis_conn.get('sex'))
#
# # print(result)
# for i in result:
#     print(i.decode('utf-8'))
#
# print(redis_conn.getset("name1", "李四1"))
# print(redis_conn.get('user').decode('utf-8'))
#
values = [['sex', '2'], ['3', '4']]

with redis_conn.pipeline(transaction=False) as p:
    for i in values:
        print(i[0], i[1])
        p.sadd(str(i[0]), str(i[1]))
    p.execute()
    # print(redis_conn.get(sex))

redis_conn.close()
