import time
import asyncio

async def send_message(msg):
    for i in range(len(msg)):
       await asyncio.sleep(1)
       print(msg[i])
    return

async def main():
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

    all_task = []
    for i in customers:
        t = loop.create_task(send_message(i))
        all_task.append(t)
    await asyncio.wait(all_task)
    return

if __name__ == "__main__":
    from datetime import datetime
    t1 = datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print("Total time taken:",datetime.now() - t1)