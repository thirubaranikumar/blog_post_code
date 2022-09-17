import time
from redis import Redis
from rq import Queue
from queue_task import send_message

redis = Redis(host='localhost', port=6379, db=0)
queue = Queue('default', connection=redis)

if __name__ == "__main__":
    customers = [
        ["Hi John",
         "Thank you for shopping with us",
         "Hope you enjoy wearing your new pair of shoes",
         "Interested to know how your purchasing experience was."],
        ["Hi Jack",
         "Thank you for shopping with us",
         "Hope you will like the fresh coffee ordered",
         "Looking to hear from you after your first cup of coffee."],
        ["Hi Jim",
         "Thank you for shopping with us",
         "Your new mobile is on the way.",
         "Hope to have your review featured on our verified customers page."]
        ]
    from datetime import datetime
    t1 = datetime.now()
    for i in customers:
        queue.enqueue(send_message, i, result_ttl=-1)
    print("Total time taken:",datetime.now() - t1)