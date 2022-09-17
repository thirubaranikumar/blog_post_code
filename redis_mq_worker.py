#redis_mq_worker.py

from redis import Redis
from rq import Queue
from rq.worker import Worker

# Returns all workers registered in this connection
redis = Redis(host='localhost',port=6379, db = 0)

# Returns all workers in this queue
queue = Queue('default',connection=redis)
worker1 = Worker(queue, connection=redis)
worker1.work()