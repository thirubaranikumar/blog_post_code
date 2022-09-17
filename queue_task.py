import time
def send_message(msg):
    for i in range(len(msg)):
       time.sleep(1)
       print(msg[i])