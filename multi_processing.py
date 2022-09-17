import time
import multiprocessing

def send_message(msg):
    for i in range(len(msg)):
       time.sleep(1)
       print(msg[i])

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
    all_process = []
    print(multiprocessing.cpu_count())
    for i in customers:
        p = multiprocessing.Process(target=send_message,args=(i,))
        all_process.append(p)
        p.start()

    for p in all_process:
        p.join()
    print("Total time taken:",datetime.now() - t1)