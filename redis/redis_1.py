import redis

redis_conn = redis_conn = redis.Redis(host='192.168.1.133', port=6379, password='123456', db=0)
redis_conn.set("123", "123")
print(redis_conn.get("123"))