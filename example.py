#!/usr/bin/env python

from redistimeseries.client import Client as RedisTimeSeries
import redis
import time

redis_host = "localhost"
redis_port = 6379

rts = RedisTimeSeries(host=redis_host, port=redis_port)



pool = redis.ConnectionPool(host=redis_host, port=redis_port)
r = redis.Redis(connection_pool=pool)

try:
    r.xadd("mystream",  {'event_type': 'startup', 'user': 'root'})
    r.xgroup_create("mystream", "consumerGroup", '$')
except:
    print("group already exists")

while True:
    msgs = r.xreadgroup("consumerGroup", "consumerName", streams={"mystream": '>'}, count=10, block=1000, noack=False)
    for msg in msgs:
        for m in msg[1]:
            evnt = m[1]['event_type']
            try:
                rts.info(evnt)
            except:
                rts.create(evnt, retentionSecs=60, labels={'event_type': evnt})
                rts.create(evnt+"_minute", retentionSecs=0, labels={'event_type': evnt})
                rts.createrule(evnt, evnt+"_minute", 'count', 60)

            rts.incrby(evnt,1)
