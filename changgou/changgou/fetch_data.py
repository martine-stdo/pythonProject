import redis
import json

redis_conn = redis.Redis(host='localhost', port=6379)

items = redis_conn.lrange('changgou:items', 0, -1)

with open('data.txt', 'w') as f:
    for item in items:
        item_dict = eval(item)
        json_text = json.dumps(item_dict, ensure_ascii=False)
        f.write(json_text + '\n')